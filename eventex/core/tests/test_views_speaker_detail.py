# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
                name='Fulano de Tal',
                slug='fulano-de-tal',
                url='http://fulanocorp.com.br',
                description='Passionate software developer!'
        )
        url = r('core:speaker_detail', kwargs={'slug': 'fulano-de-tal'})
        self.resp = self.client.get(url)

    def test_get(self):
        """GET should result in 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Template should be core/speaker_detail.html."""
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        """HTML must contain data."""
        self.assertContains(self.resp, 'Fulano de Tal')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://fulanocorp.com.br')

    def test_context(self):
        """Speaker must be in context."""
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'alonso'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
