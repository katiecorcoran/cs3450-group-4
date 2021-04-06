from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django import forms

from .forms import TotalSpaces
from .models import Lot, Reservation

class ReservationCreateView(CreateView):
    model = Reservation
    fields = ('name', 'email', 'license_plate', 'date')

    def form_valid(self, form):
        lot = get_object_or_404(Lot, pk=self.kwargs['lot_id'])
        form.instance.lot = lot
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(ReservationCreateView, self).get_form(form_class)
        form.fields['name'].widget.attrs.update({'placeholder': 'First Last'})
        form.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        form.fields['license_plate'].widget.attrs.update({'placeholder': 'XXXXXXX'})
        form.fields['date'].widget = forms.DateInput(format='%d/%m/%Y')
        form.fields['date'].widget.attrs.update({'id': 'date', 'placeholder': 'MM/DD/YYYY'})
        return form

    def get_context_data(self, **kwargs):
        ctx = super(ReservationCreateView, self).get_context_data(**kwargs)
        lot = Lot.objects.get(pk=self.kwargs['lot_id'])
        ctx['lot'] = lot
        ctx['space_type'] = self.kwargs['space_type']
        return ctx

def redirect_index(request):
    response = redirect('/parking/')
    return response

def index(request):
    context = {}
    return render(request, 'parking/index.html')

def reserve_space(request, lot_id, space_type):
    try:
        lot = Lot.objects.get(pk=lot_id)
    except Lot.DoesNotExist:
        raise Http404("Space %s does not exist." % lot_id)
    context = {'lot': lot, 'space_type': space_type}
    return render(request, 'parking/reserveSpace.html', context)

def lots(request):
    all_lots = Lot.objects.order_by('id')
    context = {'lot_list': all_lots}
    return render(request, 'parking/lots.html', context)

def lot(request, lot_id):
    try:
        lot = Lot.objects.get(pk=lot_id)
    except Lot.DoesNotExist:
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
            obj = Lot()
            obj.available_spaces = form.cleaned_data["available_spaces"]
            obj.available_spaces_lrg = form.cleaned_data["available_spaces_lrg"]
            obj.location = form.cleaned_data["location"]
            obj.nickname = form.cleaned_data["nickname"]
            obj.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/parking')



    # if a GET (or any other method) we'll create a blank form
    else:
        form = TotalSpaces()

    return HttpResponseRedirect('/parking')



