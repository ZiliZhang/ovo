from django.db import models

# Create your models here.
class Greeting(models.Model):
	when = models.DateTimeField('date created', auto_now_add=True)


class User(models.Model):
	email = models.CharField(unique=True, max_length=50)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	username = models.CharField(unique=True, max_length=15)
	password = models.CharField(max_length=8)
	birth_date = models.CharField(max_length=10)
	gender = models.CharField(max_length=6)
	age = models.PositiveIntegerField()

