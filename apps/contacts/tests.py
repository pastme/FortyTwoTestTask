from django.test import TestCase
from django.template.defaultfilters import escape, date

from contacts.models import Contacts

class ContactTest(TestCase):
    fixtures = ['initial_data.json']

    def test_contact(self):
        response = self.client.get('/contacts/1/')
        contact = Contacts.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, contact.name)
        self.assertContains(response, contact.surname)
        self.assertContains(response, escape(contact.bio))
        self.assertContains(response, date(contact.date_of_birth))
        self.assertContains(response, contact.email)
        self.assertContains(response, contact.skype)
        self.assertContains(response, contact.jabber)
        self.assertContains(response, escape(contact.contacts))

