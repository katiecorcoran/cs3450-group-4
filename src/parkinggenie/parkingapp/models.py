from django.db import models

class Lot(models.Model):
    total_spaces = models.IntegerField(default=0)
    available_spaces = models.IntegerField(default=0)
    available_spaces_lrg = models.IntegerField(default=0)
    reserved_spaces = models.IntegerField(default=0)
    location = models.CharField(default='', max_length=10000)
    nickname = models.CharField(default='', max_length=10000)
