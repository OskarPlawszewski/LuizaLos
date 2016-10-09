from django.db import models


class Picture(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)

# Create your models here.
