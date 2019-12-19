from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.

# class Category:
#     def __init__(self, name):
#       self.name = name

CATEGORIES = (
    ('outdoors', 'Outdoors'),
    ('entertainment', 'Entertainment'),
    ('food', 'Food'),
    ('tech', 'Tech'),
    ('education', 'Education'),
    ('health', 'Health'),
)

class Event(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField('event date')
    time = models.TimeField('event time')
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    attendees = ArrayField(models.CharField(max_length=250))
    infolink = models.CharField(max_length=1000)
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=100,
        choices=CATEGORIES,
    )
=======
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> e65c4c65bdea7279128db3ba251af4550a15a818

    def get_absolute_url(self):
        return reverse('events_detail', kwargs={'event_id': self.id})

    


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     id = GoogleId
#     events = Event
#     comments = Comment

