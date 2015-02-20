from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, USZipCodeField

class FreeStuff(models.Model):
    FREE_CHOICES=[('T-shirt','T-shirt'),('Sticker','Sticker'),('Keychain','Keychain')]
    name = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256, default="")
    address = models.CharField(max_length=256, default="")
    state = USStateField(choices = STATE_CHOICES)
    zipcode = USZipCodeField(max_length=None)
    gift = models.CharField(max_length=10, choices=FREE_CHOICES)
    def __unicode__(self):
        return self.name

    #When making changes to class 
    #!.) python manage.py makemigrations main
	#2.) python manage.py migrate

class Candidate(models.Model):
    name=models.CharField(max_length=100, default="")
    party=models.CharField(max_length=10, default="")
    description=models.TextField(default="Description here")
    picture=models.CharField(max_length=100, default="")
    def __unicode__(self):
        return self.name

