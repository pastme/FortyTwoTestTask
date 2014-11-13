from django.db import models
from PIL import Image

class Contacts(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    date_of_birth = models.DateField()
    bio = models.TextField()
    contacts = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photoes', null=True)

    def save(self):
        if not self.photo:
            return
        super(Contacts, self).save()
        image = Image.open(self.photo)
        (width, height) = image.size
        if width > height and width != 200:
            ratio = height/float(width)
            width = 200
            height = int(200*ratio)
        elif height > width and height != 200:
            ratio = width/float(height)
            height = 200
            width = int(200*ratio)
        size = ( width, height)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)


class RequestData(models.Model):
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)