# -*- coding: utf8 -*-
from datetime import datetime

from django.utils import unittest, timezone
from django.test.utils import override_settings

from basis.compat import get_user_model
from .models import Person


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
        person = Person()
        person.save(current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

    def test_create_person_without_user(self):
        person = Person.objects.create()

        self.assertEqual(person.created_by, None)
        self.assertEqual(person.updated_by, None)

    def test_create_person_with_user(self):
        person = Person.objects.create(current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

    def test_update_person_with_user(self):
        person = Person.objects.create(current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

        person.save(current_user=self.user2)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user2)

    def test_delete_person(self):
        person = Person.objects.create(current_user=self.user1)

        self.assertEqual(Person.objects.all().count(), 1)
        person.delete()
        self.assertEqual(Person.objects.all().count(), 0)
        self.assertEqual(Person.all_objects.all().count(), 1)

        person.restore()
        self.assertEqual(Person.objects.all().count(), 1)
