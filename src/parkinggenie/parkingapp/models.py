from django.db import models
from django.urls import reverse

class EventSpaces(models.Model):
    total_spaces = models.IntegerField(default=0)
    available_spaces = models.IntegerField(default=0)
    available_spaces_lrg = models.IntegerField(default=0)
    location = models.CharField(default='', max_length=10000)
    nickname = models.CharField(default='', max_length=10000)
    price = models.IntegerField(default=0)
    Event = models.ForeignKey("Event", on_delete=models.CASCADE)

class Reservation(models.Model):
    lot = models.ForeignKey("EventSpaces", on_delete=models.CASCADE)
    name = models.CharField(default='',max_length=100)
    email = models.EmailField(max_length=254)
    date = models.DateField()
    license_plate = models.CharField(default='', max_length=8)

class Event(models.Model):
    name = models.CharField(default='',max_length=100)
    date = models.DateField()
    location = models.CharField(default='',max_length=1000)

