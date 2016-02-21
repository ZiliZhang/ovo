from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
class User2(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
class User3(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
class User4(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

