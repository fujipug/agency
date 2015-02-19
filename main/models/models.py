from django.db import models
from us_states import STATE_CHOICES
from localflavor.us.models import USStateField


class FreeStuff(models.Model):
    FREE_CHOICES=[('T-shirt','T-shirt'),('Sticker','Sticker'),('Keychain','Keychain')]
    name = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256, default="")
    address = models.CharField(max_length=256, default="")
    state = models.USStateField(attrs=None)
    zipcode = models.CharField(max_length=6, default="")
    gift = models.CharField(max_length=10, choices=FREE_CHOICES, default='T-shirt')
    def __unicode__(self):
        return self.name

    #When making changes to class 
    #!.) python manage.py makemigrations main
	#2.) python manage.py migrate

class Candidate(models.Model):
    name=models.TextField(default="")
    party=models.CharField(max_length=10, default="")
    description=models.TextField(default="Description missing.")
    picture=models.TextField(default="")
    def __unicode__(self):
        return self.name

    #Still have to add to DB