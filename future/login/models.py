from django.db import models

# Create your models here.

class UserGroup(models.Model):
    department = models.CharField(max_length=256)
    position_id = models.IntegerField(default=1)
    position = models.CharField(max_length=256)

class User(models.Model):
    gender = (('male', '男'), ('female', '女'))
    name = models.CharField(max_length=123, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)
    G = models.ForeignKey(to_field='id', to="UserGroup", on_delete=models.CASCADE, default=1)
