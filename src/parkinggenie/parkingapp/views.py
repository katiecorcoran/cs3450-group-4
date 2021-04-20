from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
import qrcode
from django import forms

from django import forms
from django.urls import reverse

from .forms import TotalSpaces, SignUp, Event
from .models import EventSpaces, Reservation, Event, UserAccount


class UserAccountView(UpdateView):
    model = UserAccount
    fields = ('balance',)

    def get_context_data(self, **kwargs):
        ctx = super(UserAccountView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            reservations = self.request.user.reservation_set.all()
            ctx['reservations'] = reservations
            ctx['currentBalance'] = self.request.user.useraccount.balance
        return ctx

    def get_form(self, form_class=None):
        form = super(UserAccountView, self).get_form(form_class)
        form.fields['balance'].widget.attrs.update({'step': 1.0})
        return form

    def get_success_url(self):
        return reverse('profilePage', kwargs={'pk': self.request.user.useraccount.id})
        

class ReservationCreateView(CreateView):
    model = Reservation
    fields = ('name', 'email', 'license_plate','space_type')

    def get_initial(self):
        return {'space_type': self.kwargs['space_type']}

    def form_valid(self, form):
        lot = get_object_or_404(EventSpaces, pk=self.kwargs['pk'])
        if form.instance.space_type == "std":
            lot.available_spaces -= 1
        elif form.instance.space_type == "lrg":
            lot.available_spaces_lrg -= 1
        lot.save()
        form.instance.lot = lot
        form.instance.event = lot.Event
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(ReservationCreateView, self).get_form(form_class)
        if self.request.user.is_authenticated:
            form.fields['name'].widget.attrs.update({'value': self.request.user.first_name + " " + self.request.user.last_name})
            form.fields['email'].widget.attrs.update({'value': self.request.user.email})
        else:
            form.fields['name'].widget.attrs.update({'placeholder': 'First Last'})
            form.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        form.fields['license_plate'].widget.attrs.update({'placeholder': 'XXXXXXX'})
        return form

    def get_context_data(self, **kwargs):
        ctx = super(ReservationCreateView, self).get_context_data(**kwargs)
        lot = EventSpaces.objects.get(pk=self.kwargs['pk'])
        ctx['lot'] = lot
        ctx['space_type'] = self.kwargs['space_type']
        ctx['event'] = lot.Event
        return ctx

    def get_success_url(self):
        return reverse('reservation-success', kwargs={'id': self.object.id})

def redirect_index(request):
    if (request.user.is_authenticated):
        response = redirect('/parking/profile/{0}'.format(request.user.useraccount.id))
    else:
        response = redirect('/parking/accounts/login')
    return response

def index(request):
    context = {}
    return render(request, 'parking/index.html')

def success(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    lot = get_object_or_404(EventSpaces, pk=reservation.lot_id)
    img = qrcode.make(f'/parking/reservation-success/{reservation.id}')
    img.save(f'parkingapp/static/images/confirmation.png')
    context = {'reservation': reservation, 'lot': lot, 'event': lot.Event}
    return render(request, 'parking/reserveSuccess.html', context)

def lots(request, event_id):
    event = get_object_or_404(Event,pk=event_id)
    all_lots = event.eventspaces_set.all()
    context = {'lot_list': all_lots}
    return render(request, 'parking/lots.html', context)

def events(request):
    all_events = Event.objects.order_by('date')
    context = {'event_list': all_events}
    return render(request, 'parking/events.html', context)

def lot(request, lot_id):
    lot = get_object_or_404(EventSpaces, pk=lot_id)
    context = {'lot': lot}
    return render(request, 'parking/lot.html', context)

def owner(request):
    context = {}
    form = TotalSpaces()
    return render(request, 'parking/owner.html', {'form': form})

def event(request):
    context = {}
    form = Event()
    return render(request, 'parking/addEvent.html', {'form': form})

def get_events(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = event(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Event()
            obj.name = form.cleaned_data["name"]
            obj.date = form.cleaned_data["date"]
            obj.location = form.cleaned_data["location"]

        else:
            print(form.errors)

            # redirect to a new URL:
            return HttpResponseRedirect('/parking')
def get_TotalSpaces(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TotalSpaces(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = EventSpaces()
            obj.available_spaces = form.cleaned_data["available_spaces"]
            obj.available_spaces_lrg = form.cleaned_data["available_spaces_lrg"]
            obj.location = form.cleaned_data["location"]
            obj.nickname = form.cleaned_data["nickname"]
            obj.Event = form.cleaned_data["event"]
            obj.price = form.cleaned_data["price"]
            obj.save()
        else:
            print(form.errors)

            # redirect to a new URL:
            return HttpResponseRedirect('/parking')



    # if a GET (or any other method) we'll create a blank form
    else:
        form = TotalSpaces()

    return HttpResponseRedirect('/parking')

def signup(request):
    context = {}
    form = SignUp()
    return render(request, 'registration/signup.html', {'form': form})

def create_Account(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            #adds the user into the database

            user = User.objects.create_user(username=form.cleaned_data["username"],
                                            first_name=form.cleaned_data["first_name"],
                                            last_name=form.cleaned_data["last_name"],
                                            email=form.cleaned_data["email"],
                                            password=form.cleaned_data["password"])
            user.save()
            userAcct = UserAccount.objects.create(user=user)
            #returns the user to the login page after making an account
    return HttpResponseRedirect('/parking/accounts/login/')
