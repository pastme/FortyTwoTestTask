from django.shortcuts import render
from django.utils.decorators import method_decorator
from apps.contacts.models import Contacts
from apps.contacts.forms import EditContactForm
from django.views.generic import DetailView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


class ViewContact(DetailView):
    model = Contacts
    pk_url_kwarg = 'contact_id'
    template_name = 'contacts/view.html'


class EditContact(UpdateView):
    model = Contacts
    form_class = EditContactForm
    template_name = 'contacts/edit.html'
    success_url =  '/'
    pk_url_kwarg = 'contact_id'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditContact, self).dispatch(*args, **kwargs)



# Create your views here.
