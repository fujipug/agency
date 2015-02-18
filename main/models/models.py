from django.db import models
 
class PostForm(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=6)

    #When making changes to class PostForm
    #!.) python manage.py makemigrations making
	#2.) python manage.py migrate