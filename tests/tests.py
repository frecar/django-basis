# -*- coding: utf8 -*-
from django.utils import unittest
from basis.compat import get_user_model
from .models import Person


class TestLoginCodes(unittest.TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.get_or_create(username="test1")[0]
        self.user2 = get_user_model().objects.get_or_create(username="test2")[0]

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

        Person.all_objects.all().delete()

    def test_crate_person_without_user(self):
        person = Person()
        person.save()

        self.assertEqual(person.created_by, None)
        self.assertEqual(person.updated_by, None)

    def test_create_person_with_user(self):

        person = Person()
        person.save(current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

    def test_update_person_with_user(self):

        person = Person()
        person.save(current_user=self.user1)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user1)

        person.save(current_user=self.user2)

        self.assertEqual(person.created_by, self.user1)
        self.assertEqual(person.updated_by, self.user2)

    def test_delete_person(self):

        person = Person()
        person.save(current_user=self.user1)

        self.assertEqual(Person.objects.all().count(), 1)
        person.delete()
        self.assertEqual(Person.objects.all().count(), 0)
        self.assertEqual(Person.all_objects.all().count(), 1)

        person.restore()
        self.assertEqual(Person.objects.all().count(), 1)
