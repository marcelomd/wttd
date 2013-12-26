# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(
                name='Fulano de Tal',
                slug='fulano-de-tal',
                url='http://fulanocorp.com.br',
                description='Passionate software developer'
        )
        self.speaker.save()

    def test_create(self):
        """Speaker instance should be saved."""
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        """Speaker string representation should be the name."""
        self.assertEqual(u'Fulano de Tal', unicode(self.speaker))


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
                name='Fulano de Tal',
                slug='fulano-de-tal',
                url='http://fulanocorp.com.br',
                description='Passionate software developer'
        )

    def test_email(self):
        contact = Contact.objects.create(
                speaker=self.speaker,
                kind='E',
                value='fulano@email.com'
        )
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(
                speaker=self.speaker,
                kind='P',
                value='11-2233445566'
        )
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(
                speaker=self.speaker,
                kind='F',
                value='11-2233445566'
        )
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        """Contact kind should be limited to E, P, F."""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        """Contact string representation should be value."""
        contact = Contact.objects.create(
                speaker=self.speaker,
                kind='E',
                value='fulano@email.com'
        )
        self.assertEqual(u'fulano@email.com', unicode(contact))

