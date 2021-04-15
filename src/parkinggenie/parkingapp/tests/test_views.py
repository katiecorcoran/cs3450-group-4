import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from parkingapp.models import EventSpaces, Reservation, Event


class ViewsTestCase(TestCase):
    def test_reservation_process(self):
        # Views with no arguments
        response = self.client.get(reverse('index'), follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)

        # No event
        response = self.client.get(reverse('lots',kwargs={'event_id':0}))
        self.assertEqual(response.status_code, 404)

        event = Event.objects.create(name="Basketball",date=datetime.date.today(),location="Spectrum")
        event.save()

        response = self.client.get(reverse('lots',kwargs={'event_id':event.id}))
        self.assertEqual(response.status_code, 200)

        # No lot
        response = self.client.get(reverse('lot',kwargs={'lot_id':0}))
        self.assertEqual(response.status_code, 404)

        spaces = EventSpaces.objects.create(total_spaces=10,available_spaces=6,available_spaces_lrg=4,location="E 1000 N",price=5,nickname="Test Lot",Event=event)
        spaces.save()

        response = self.client.get(reverse('lot',kwargs={'lot_id':spaces.id}))
        self.assertEqual(response.status_code, 200)  

        response = self.client.post(
            reverse('reserve',kwargs={'pk':spaces.id,'space_type':'std'}),
            data={'lot': spaces, 'name': 'Jane Doe', 'email': 'noone@nowhere.com', 'license_plate': '1234567', 'space_type': 'std'}    
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/parking/reservation-success/1')

        # Invalid reservation
        response = self.client.get(reverse('reservation-success',kwargs={'id':0}))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(reverse('reservation-success',kwargs={'id':1}))
        self.assertEqual(response.status_code, 200)

    def test_user_views(self):
        # Sign up dummy user
        response = self.client.post(
            reverse('createaccount'),
            data={'username':'dummy','first_name':'Jane','last_name':'Doe','email':'noone@nowhere.com','password':'dummy123'}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/parking/accounts/login/')

        response = self.client.login(username='dummy',password='dummy123')
        self.assertEqual(response, True)

        response = self.client.get(reverse('profilePage'))
        self.assertEqual(response.status_code, 200)

        # Add models to make a reservation
        event = Event.objects.create(name="Basketball",date=datetime.date.today(),location="Spectrum")
        event.save()

        response = self.client.get(reverse('owner'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('addingspace'),
            data={'event':1,'available_spaces':6,'available_spaces_lrg':4,'location':'Location','nickname':'Test Lot','price':5}
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/parking')

        spaces = EventSpaces.objects.get(pk=1)
        user = User.objects.filter(username='dummy')[0]

        response = self.client.post(
            reverse('reserve',kwargs={'pk':spaces.id,'space_type':'std'}),
            data={'user':user,'lot': spaces, 'name': 'Jane Doe', 'email': 'noone@nowhere.com', 'license_plate': '1234567', 'space_type':'std'},
            follow=True    
        )

        self.assertEqual(response.status_code, 200)

        savedReservation = Reservation.objects.get(pk=1)
        self.assertEqual(savedReservation.user.id, user.id)

        