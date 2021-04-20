from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class EventSpaces(models.Model):
    total_spaces = models.IntegerField(default=0)
    available_spaces = models.IntegerField(default=0)
    available_spaces_lrg = models.IntegerField(default=0)
    location = models.CharField(default='', max_length=10000)
    nickname = models.CharField(default='', max_length=10000)
    price = models.IntegerField(default=0)
    Event = models.ForeignKey("Event", on_delete=models.CASCADE)

class Reservation(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    lot = models.ForeignKey("EventSpaces", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(default='',max_length=100)
    email = models.EmailField(max_length=254)
    space_type = models.CharField(max_length=10, choices = (('std','Standard'), ('lrg','Large')))
    license_plate = models.CharField(default='', max_length=8)

class Event(models.Model):
    name = models.CharField(default='',max_length=100)
    date = models.DateField()
    location = models.CharField(default='',max_length=1000)

    def __str__(self):
        return self.name

class UserAccount(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   balance = models.DecimalField(max_digits=6, decimal_places=2, default=0)

