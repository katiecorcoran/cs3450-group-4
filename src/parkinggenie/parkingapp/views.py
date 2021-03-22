from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TotalSpaces
from .models import Space, Lot

def redirect_index(request):
    response = redirect('/parking/')
    return response

def index(request):
    context = {}
    return render(request, 'parking/index.html')

def spaces(request, lot_id):
    return HttpResponse("You're viewing spaces in lot %s." % lot_id)

def reserve_space(request, space_id):
    return HttpResponse("You're trying to reserve space %s." % space_id)

def lots(request):
    all_lots = Lot.objects.order_by('id')
    context = {'lot_list': all_lots}
    return render(request, 'parking/lots.html', context)

def lot(request, lot_id):
    try:
        lot = Lot.objects.get(pk=lot_id)
        lot_spaces = Space.objects.filter(lot=lot_id)
    except Lot.DoesNotExist:
        raise Http404("Lot %s does not exist." % lot_id)
    context = {'lot': lot}
    return render(request, 'parking/lot.html', context)

def owner(request):
    context = {}
    return render(request,'parking/owner.html')


def get_TotalSpaces(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TotalSpaces(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TotalSpaces()

    return render(request, 'parking/owner.html', {'form': form})
def addingspace(request):
    new_lot = lot (total_spaces="0", available_spaces="0" , reserved_spaces="0")
    new_lot.save()
