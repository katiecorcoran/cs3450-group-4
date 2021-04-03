from django.contrib import admin

from .models import Lot, Reservation

admin.site.register(Lot)
admin.site.register(Reservation)
