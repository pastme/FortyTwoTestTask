from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    date_of_birth = models.DateField()
    bio = models.TextField()
    contacts = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)