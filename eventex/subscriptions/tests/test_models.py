# coding: utf-8
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription

class Subscriptiontest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='Fulano de Tal',
                cpf='12345678901',
                email='fulano@email.com',
                phone='112233445566'
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
        self.assertEqual(u'Fulano de Tal', unicode(self.obj))

    def test_paid_default_value_is_false(self):
        """Default must be false."""
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
                name='Fulano de Tal',
                cpf='12345678901',
                email='fulano@email.com',
                phone='112233445566'
        )

    def test_cpf_unique(self):
        """CPF must be unique."""
        s = Subscription(
                name='Fulano de Tal',
                cpf='12345678901',
                email='other@email.com',
                phone='112233445566'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
        """Email is not unique anymore."""
        s = Subscription.objects.create(
                name='Fulano de Tal',
                cpf='23456789012',
                email='fulano@email.com')
        self.assertEqual(2, s.pk)
