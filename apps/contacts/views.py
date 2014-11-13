from django.shortcuts import render
from django.utils.decorators import method_decorator
from apps.contacts.models import Contacts,RequestData
from apps.contacts.forms import EditContactForm
from django.views.generic import DetailView, UpdateView,ListView
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


class ListRequests(ListView):
    model = RequestData
    template_name = 'requests/view.html'


    def get_queryset(self):
        return super(ListRequests, self).get_queryset().order_by('timestamp')[:10]

# Create your views here.
