from django.test import TestCase, RequestFactory
from django.template.defaultfilters import escape, date, linebreaks
from apps.contacts.middleware import RequestToDbMiddleware
from django.contrib.auth.models import AnonymousUser

from contacts.models import Contacts, RequestData

class ContactTest(TestCase):
    fixtures = ['initial_data.json']

    def test_contact(self):
        response = self.client.get('')
        contact = Contacts.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, contact.name)
        self.assertContains(response, contact.surname)
        self.assertContains(response, linebreaks(escape(contact.bio)))
        self.assertContains(response, date(contact.date_of_birth))
        self.assertContains(response, contact.email)
        self.assertContains(response, contact.skype)
        self.assertContains(response, contact.jabber)
        self.assertContains(response, linebreaks(escape(contact.contacts)))

class ContactEditTest(TestCase):
    def logout(self):
        self.client.logout()

    def test_login(self):
        response = self.client.get('/edit/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='100362')
        response = self.client.get('/edit/')
        self.assertEqual(response.status_code, 200)

    def test_form_get(self):
        contact = Contacts.objects.get(pk=1)
        self.client.login(username='admin', password='100362')
        response = self.client.get('/edit/')

        self.assertContains(response, contact.name)
        self.assertContains(response, contact.surname)
        self.assertContains(response, contact.date_of_birth)
        self.assertContains(response, contact.email)
        self.assertContains(response, contact.skype)
        self.assertContains(response, contact.jabber)
        self.assertContains(response, contact.bio)
        self.assertContains(response, contact.contacts)

    def test_form_post(self):
        contact = {}
        contact['name'] = 'Tester'
        contact['surname'] = 'Testovich'
        contact['date_of_birth'] = '1992-11-03'
        contact['email'] = 'tester@test.com'
        contact['jabber'] = 'jabtest@test.com'
        contact['skype'] = 'testik'
        contact['bio'] = "I was born in testland by mighty testers."
        contact['contacts'] = "mobile: 09707070707"

        self.client.login(username='admin', password='100362')
        response = self.client.post('/edit/', contact, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, contact['name'])
        self.assertContains(response, contact['surname'])
        self.assertContains(response, date(contact['date_of_birth']))
        self.assertContains(response, contact['email'])
        self.assertContains(response, contact['jabber'])
        self.assertContains(response, contact['skype'])
        self.assertContains(response, escape(contact['bio']))
        self.assertContains(response, escape(contact['contacts']))




class MiddlewareCountTest(TestCase):

    def test_storing(self):
        for i in range(10):
            self.client.get('')
        requests = RequestData.objects.all()
        self.assertEqual(requests.count(), 10)

    def tearDown(self):
        RequestData.objects.all().delete()


class RequestToDbMiddlewareTest(TestCase):

    def setUp(self):
        RequestData.objects.all().delete()
        self.rm = RequestToDbMiddleware()
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_process_request_for_middleware(self):
        request = self.factory.get('/')
        self.rm.process_request(request)
        request_data = RequestData.objects.get()
        self.assertEqual(str(request), request_data.data)

