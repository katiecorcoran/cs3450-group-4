from django.contrib import admin

from .models import Event, EventSpaces, Reservation, UserAccount

admin.site.register(EventSpaces)
admin.site.register(Reservation)
admin.site.register(Event)
admin.site.register(UserAccount)
