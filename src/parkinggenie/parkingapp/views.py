from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

<<<<<<< HEAD
from .forms import TotalSpaces
from .models import Space, Lot
=======
from .models import Lot
>>>>>>> 58f5834dc04294ff29adba67307ae90f29a84597

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
            obj.total_spaces = form.cleaned_data["total_spaces"]
            obj.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/parking')



    # if a GET (or any other method) we'll create a blank form
    else:
        form = TotalSpaces()

    return HttpResponseRedirect('/parking')



