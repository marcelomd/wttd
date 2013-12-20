# coding: utf-8
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription

class Subscriptiontest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='Marcelo MD',
                cpf='12345678901',
                email='md@marcelomd.com',
                phone='51-81218871'
        )

    def test_create(self):
        """Subscriptions must havename, cpf, email, phone."""
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        """Subscription must have automatic created at."""
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        """Must handle unicode."""
        self.assertEqual(u'Marcelo MD', unicode(self.obj))

    def test_paid_default_value_is_false(self):
        """Default must be false."""
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
                name='Marcelo MD',
                cpf='12345678901',
                email='md@marcelomd.com',
                phone='51-81218871'
        )

    def test_cpf_unique(self):
        """CPF must be unique."""
        s = Subscription(name='Marcelo MD',
                cpf='12345678901',
                email='bla@marcelomd.com',
                phone='51-81218871',
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        """Email must be unique."""
        s = Subscription(name='Marcelo MD',
                cpf='00000000001',
                email='md@marcelomd.com',
                phone='51-81218871',
        )
        self.assertRaises(IntegrityError, s.save)

