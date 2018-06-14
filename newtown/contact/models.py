from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	title= models.CharField(max_length=50)
	message = models.TextField()
	timestamp = models.DateTimeField()
# Create your models here.
