from django.conf.urls import patterns, url

from apps.contacts import views

urlpatterns = patterns('',

    # Contacts
    url(r'^$',views.ViewContact.as_view(),
        {'contact_id': 1},
        name='view_contact'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login',
        name='auth_logout'),
    url(r'^edit/$',views.EditContact.as_view(),
        {'contact_id': 1},
        name='edit_contact'),
    url(r'^requests/$',views.ListRequests.as_view(),
        name='requests'),


)