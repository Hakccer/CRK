from django.db import models

# Create your models here.


class Store(models.Model):
    userid = models.TextField()
    title = models.TextField()
    passes = models.TextField()
    date = models.DateField()


class Room(models.Model):
    name = models.TextField()
    usenum = models.IntegerField(default=0)


class Messaging(models.Model):
    userid = models.TextField()
    message = models.TextField()
    date = models.DateField()
    roo_name = models.TextField(default='anon', null=False)
