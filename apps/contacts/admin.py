from django.contrib import admin
from apps.contacts.models import Contacts, RequestData
# Register your models here.
admin.site.register(Contacts)
admin.site.register(RequestData)