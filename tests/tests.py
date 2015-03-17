# -*- coding: utf8 -*-
import sys
from datetime import datetime

from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory

from django.utils import unittest, timezone
from django.test.utils import override_settings

from basis.compat import get_user_model
from .models import Person
from .views import BasisModelViewSet

PY3 = sys.version_info[0] == 3

if PY3:
    from unittest import mock
else:
    import mock


class TestTimeStampModel(unittest.TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.get_or_create(username="test1")[0]
        self.user2 = get_user_model().objects.get_or_create(username="test2")[0]

    def tearDown(self):
        get_user_model().objects.all().delete()
        Person.all_objects.all().delete()

    def test_datetimes(self):
        person = Person.objects.create(current_user=self.user1)

        self.assertAlmostEqual(int(person.created_at.strftime('%Y%m%d%H%M%S')),
                               int(datetime.now().strftime('%Y%m%d%H%M%S')))
        person.save()
        self.assertNotEqual(person.created_at, person.updated_at)
        self.assertAlmostEqual(int(person.updated_at.strftime('%Y%m%d%H%M%S')),
                               int(datetime.now().strftime('%Y%m%d%H%M%S')))

    @override_settings(USE_TZ=True)
    def test_datetimes_with_timezone(self):
        person = Person.objects.create(current_user=self.user1)
        self.assertEqual(person.created_at.tzinfo, timezone.utc)
        self.assertEqual(person.updated_at.tzinfo, timezone.utc)

        self.assertAlmostEqual(int(person.created_at.strftime('%Y%m%d%H%M%S')),
                               int(timezone.now().strftime('%Y%m%d%H%M%S')))
        person.save()
        self.assertNotEqual(person.created_at, person.updated_at)
        self.assertAlmostEqual(int(person.updated_at.strftime('%Y%m%d%H%M%S')),
                               int(timezone.now().strftime('%Y%m%d%H%M%S')))


class TestPersistentModel(unittest.TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.get_or_create(username='test1')[0]
        self.user2 = get_user_model().objects.get_or_create(username='test2')[0]

    def tearDown(self):
        get_user_model().objects.all().delete()
        Person.all_objects.all().delete()

    def test_delete_person(self):
        person = Person.objects.create(current_user=self.user1)

        self.assertEqual(Person.objects.all().count(), 1)
        person.delete()
        self.assertEqual(Person.objects.all().count(), 0)
        self.assertEqual(Person.all_objects.all().count(), 1)

        person.restore()
        self.assertEqual(Person.objects.all().count(), 1)
        Person.all_objects.all()[0].delete()
        self.assertEqual(Person.objects.all().count(), 0)
        self.assertEqual(Person.all_objects.all().count(), 1)

    def test_force_delete(self):
        person = Person.objects.create(current_user=self.user1)
        person.delete(force=True)
        self.assertEqual(Person.all_objects.count(), 0)

    @mock.patch('django.db.models.base.Model.delete')
    def test_delete_with_using(self, mock_delete):
        person = Person.objects.create(current_user=self.user1)
        person.delete(force=True, using='other_db')
        mock_delete.assert_called_with('other_db')


class TestBasisModel(unittest.TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.get_or_create(username="test1")[0]
        self.user2 = get_user_model().objects.get_or_create(username="test2")[0]

    def tearDown(self):
        get_user_model().objects.all().delete()
        Person.all_objects.all().delete()

    def test_save_person_without_user(self):
        person = Person()
        person.save()

        self.assertEqual(person.created_by, None)
        self.assertEqual(person.updated_by, None)

    def test_save_person_with_user(self):
        person = Person(name='john doe')
        person.save(current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

        person_from_db = Person.objects.get(name='john doe')
        self.assertEqual(person_from_db.created_by, self.user1)
        self.assertEqual(person_from_db.updated_by, self.user1)

    def test_create_person_without_user(self):
        person = Person.objects.create(name='john doe')

        self.assertEqual(person.created_by, None)
        self.assertEqual(person.updated_by, None)

        person_from_db = Person.objects.get(name='john doe')
        self.assertEqual(person_from_db.created_by, None)
        self.assertEqual(person_from_db.updated_by, None)

    def test_create_person_with_user(self):
        person = Person.objects.create(name='john doe', current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

        person_from_db = Person.objects.get(name='john doe')
        self.assertEqual(person_from_db.created_by, self.user1)
        self.assertEqual(person_from_db.updated_by, self.user1)

    def test_update_person_with_user(self):
        person = Person.objects.create(name='john doe', current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

        person_from_db = Person.objects.get(name='john doe')
        self.assertEqual(person_from_db.created_by, self.user1)
        self.assertEqual(person_from_db.updated_by, self.user1)

        person.save(current_user=self.user2)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user2)

        person_from_db = Person.objects.get(name='john doe')
        self.assertEqual(person_from_db.created_by, self.user1)
        self.assertEqual(person_from_db.updated_by, self.user2)


class TestBasisSerializer(APITestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.get_or_create(username="test1")[0]
        self.user2 = get_user_model().objects.get_or_create(username="test2")[0]

        self.factory = APIRequestFactory()
        self.request_post = self.factory.post('/', {'name': 'username 123'})
        self.view_post = BasisModelViewSet.as_view({'post': 'create'})

        self.request_put = self.factory.put('/', {'name': 'username 321'})
        self.view_put = BasisModelViewSet.as_view({'put': 'update'})

    def test_created_by(self):
        force_authenticate(self.request_post, user=self.user1)
        response = self.view_post(self.request_post)

        self.assertEqual(response.data['created_by'], self.user1.pk)
        self.assertEqual(response.data['updated_by'], self.user1.pk)

    def test_updated_by(self):
        user = Person(name="username 123")
        user.save(current_user=self.user1)
        id = user.pk

        force_authenticate(self.request_put, user=self.user2)
        response = self.view_put(self.request_put, pk=id)

        self.assertNotEqual(response.data['created_by'], self.user2.pk)
        self.assertEqual(response.data['updated_by'], self.user2.pk)
