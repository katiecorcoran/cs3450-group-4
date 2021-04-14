import datetime

from django.test import TestCase
from parkingapp.models import EventSpaces, Reservation, Event

class ModelsTestCase(TestCase):
    def test_models(self):
        event = Event.objects.create(name="Basketball",date=datetime.date.today(),location="Spectrum")
        event.save()

        savedEvent = Event.objects.filter(name="Basketball")[0]
        self.assertNotEqual(savedEvent, None)
        self.assertEqual(savedEvent.date, datetime.date.today())
        self.assertEqual(savedEvent.location, "Spectrum")

        spaces = EventSpaces.objects.create(total_spaces=10,available_spaces=6,available_spaces_lrg=4,location="E 1000 N",price=5,nickname="Test Lot",Event=event)
        spaces.save()

        savedSpaces = EventSpaces.objects.filter(nickname="Test Lot")[0]
        self.assertNotEqual(savedSpaces, None)
        self.assertEqual(savedSpaces.total_spaces, 10)
        self.assertEqual(savedSpaces.available_spaces, 6)
        self.assertEqual(savedSpaces.available_spaces_lrg, 4)
        self.assertEqual(savedSpaces.location, "E 1000 N")
        self.assertEqual(savedSpaces.price, 5)
        self.assertEqual(savedSpaces.Event.id, savedEvent.id)

        reservation = Reservation.objects.create(lot=savedSpaces,name="Jane Doe",email="noone@nowhere.com",license_plate="1111111")
        reservation.save()

        savedReservation = Reservation.objects.filter(name="Jane Doe")[0]
        self.assertNotEqual(savedReservation, None)
        self.assertEqual(savedReservation.lot, savedSpaces)
        self.assertEqual(savedReservation.email, "noone@nowhere.com")
        self.assertEqual(savedReservation.license_plate, "1111111")