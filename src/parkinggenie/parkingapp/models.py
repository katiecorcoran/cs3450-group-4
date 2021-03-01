from django.db import models

class Lot(models.Model):
    total_spaces = models.IntegerField(default=0)
    available_spaces = models.IntegerField(default=0)
    reserved_spaces = models.IntegerField(default=0)

class Space(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)
    cost = models.IntegerField(default=0)
