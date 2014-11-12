from django import forms
from apps.contacts.models import Contacts

class EditContactForm(forms.ModelForm):

    class Meta:
        model = Contacts