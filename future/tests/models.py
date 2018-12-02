from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.Charfield(max_length=30 , primary_key = True)
    username = models.Charfield(max_length=30)
    password = models.Charfield(max_length=30)
    email = models.EmailField()

class Group(models.Model):
    groupid = models.Charfield(max_length=30, primary_key = True)
    userid = models.Charfield(max_length=30)
    department = models.Charfield(max_length=30)

class authorityinfo(models.Model):
    authorityid = models.Charfield(max_length=30, primary_key = True)
    authorityname = models.Charfield(max_length=30)

class authority(models.Model):
    userid = models.Charfield(max_length=30)
    groupid = models.Charfield(max_length=30)
    authorityid = models.Charfield(max_length=30)