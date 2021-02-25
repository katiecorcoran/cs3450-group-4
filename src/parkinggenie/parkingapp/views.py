from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Space, Lot

def index(request):
    return HttpResponse("Hello, world. This is the parking genie site index.")

def spaces(request, lot_id):
    return HttpResponse("You're viewing spaces in lot %s." % lot_id)

def reserve_space(request, space_id):
    return HttpResponse("You're trying to reserve space %s." % space_id)

def lots(request):
    all_lots = Lot.objects.order_by('id')
    context = {'lot_list': all_lots}
    return render(request, 'parking/index.html', context)

def lot(request, lot_id):
    try:
        lot = Lot.objects.get(pk=lot_id)
        lot_spaces = Space.objects.filter(lot=lot_id)
    except Lot.DoesNotExist:
        raise Http404("Lot %s does not exist." % lot_id)
    context = {'lot': lot}
    return render(request, 'parking/lot.html', context)