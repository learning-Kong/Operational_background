from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.Charfield(max_length=30)
