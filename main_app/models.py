from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.

# class Category:
#     def __init__(self, name):
#       self.name = name

class Event(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField('event date')
    time = models.TimeField('event time')
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    attendees = ArrayField(models.CharField(max_length=250))
    infolink = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     id = GoogleId
#     events = Event
#     comments = Comment

