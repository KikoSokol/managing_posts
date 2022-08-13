from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)


class Post(models.Model):
    userId = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=10000)
