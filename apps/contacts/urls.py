from django.conf.urls import patterns, url

from apps.contacts import views

urlpatterns = patterns('',

    # Contacts
    url(r'$',views.ViewContact.as_view(),
        {'contact_id': 1},
        name='view_contact'),
)