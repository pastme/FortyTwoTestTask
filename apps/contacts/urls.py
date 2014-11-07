from django.conf.urls import patterns, url

from apps.contacts import views

urlpatterns = patterns('',

    # Contacts
    url(r'^contacts/(?P<contact_id>\d+)/$',
        views.ViewContact.as_view(),
        name='view_contact'),
)