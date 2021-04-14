from django.contrib import admin

from .models import Event, EventSpaces, Reservation

admin.site.register(EventSpaces)
admin.site.register(Reservation)
admin.site.register(Event)
