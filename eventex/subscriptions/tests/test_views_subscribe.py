from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        """ Get /inscricao/ must return 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Response should be a rendered template."""
        self.assertTemplateUsed(self.resp,
                'subscriptions/subscription_form.html')

    def test_html(self):
        """ HTML must contain input controls."""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """ HTML must contain csrf token."""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have subscription form."""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """ Form must have 4 fields."""
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
                name='Fulano de Tal',
                cpf='12345678901',
                email='fulano@email.com',
                phone='112233445566'
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/1/."""
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        """Valid POST must be saved."""
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
                name='Fulano de Tal',
                cpf='123456789012',
                email='fulano@email.com',
                phone='112233445566'
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        """Invalid POST should not redirect."""
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        """Form must contain errors."""
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        """Do not save data."""
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        """Check if non_field_errors are shown in template."""
        invalid_data = dict(name='Fulano de Tal', cpf='12345678901')
        response=self.client.post(r('subscriptions:subscribe'), invalid_data)
        self.assertContains(response, '<ul class="errorlist">')
