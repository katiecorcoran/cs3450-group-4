from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User

from django import forms

from django import forms
from django.urls import reverse

from .forms import TotalSpaces, SignUp
from .models import EventSpaces, Reservation, Event

class ReservationCreateView(CreateView):
    model = Reservation
    fields = ('name', 'email', 'license_plate')

    def form_valid(self, form):
        lot = get_object_or_404(EventSpaces, pk=self.kwargs['pk'])
        form.instance.lot = lot
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(ReservationCreateView, self).get_form(form_class)
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
    response = redirect('/parking/')
    return response

def index(request):
    context = {}
    return render(request, 'parking/index.html')

def success(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    lot = get_object_or_404(EventSpaces, pk=reservation.lot_id)
    context = {'reservation': reservation, 'lot': lot, 'event': lot.Event}
    return render(request, 'parking/reserveSuccess.html', context)

def lots(request, event_id):
    event = Event.objects.get(pk=event_id)
    all_lots = event.eventspaces_set.all()
    context = {'lot_list': all_lots}
    return render(request, 'parking/lots.html', context)

def events(request):
    all_events = Event.objects.order_by('date')
    context = {'event_list': all_events}
    return render(request, 'parking/events.html', context)

def lot(request, lot_id):
    try:
        lot = EventSpaces.objects.get(pk=lot_id)
    except EventSpaces.DoesNotExist:
        raise Http404("Lot %s does not exist." % lot_id)
    context = {'lot': lot}
    return render(request, 'parking/lot.html', context)

def owner(request):
    context = {}
    form = TotalSpaces()
    return render(request, 'parking/owner.html', {'form': form})

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
            #returns the user to the login page after making an account
            return HttpResponseRedirect('/parking')


@login_required(login_url='/accounts/login/')
def profilePage(request):
    context = {'lots': []}
    return render(request, 'parking/profile.html', context)