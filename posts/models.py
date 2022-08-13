from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

def validate_title(value):
    if len(value) < 5:
        raise ValidationError("Title must contain at least 5 characters.")

    return value


class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=256, validators=[validate_title])
    body = models.CharField(max_length=100000)
