from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, default="NULL")
    username = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=8, default="NULL")
    birth_date = models.CharField(max_length=10, default="NULL")
    gender = models.CharField(max_length=6, default="NULL")
    age = models.PositiveIntegerField(default="20")
