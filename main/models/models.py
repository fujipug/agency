from django.db import models

class PostForm(models.Model):
    name = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256, default="")
    address = models.CharField(max_length=256, default="")
    state = models.CharField(max_length=2, default="")
    zipcode = models.CharField(max_length=6, default="")
    def __unicode__(self):
        return self.name

    #When making changes to class PostForm
    #!.) python manage.py makemigrations making
	#2.) python manage.py migrate

class Candidate(models.Model):
    name=models.TextField(default="")
    party=models.CharField(max_length=10, default="")
    description=models.TextField(default="Description missing.")
    picture=models.TextField(default="")
    def __unicode__(self):
        return self.name

    #Still have to add to DB