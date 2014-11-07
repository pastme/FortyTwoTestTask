from django.shortcuts import render
from apps.contacts.models import Contacts
from django.views.generic import DetailView

class ViewContact(DetailView):
    model = Contacts
    pk_url_kwarg = 'contact_id'
    template_name = 'contacts/view.html'

# Create your views here.
