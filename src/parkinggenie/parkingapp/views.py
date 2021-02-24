from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the parking genie site index.")

def space(request, space_id):
    return HttpResponse("You're viewing space %s." % space_id)

def reserve_space(request, space_id):
    return HttpResponse("You're trying to reserve space %s." % space_id)

def lot(request, lot_id):
    return HttpResponse("Viewing availability for lot %s." % lot_id)