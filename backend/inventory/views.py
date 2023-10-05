from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404
from .models import Supplies

# Create your views here.
def locate(request, item_key):
    item = get_object_or_404(Supplies, pk=item_key)

    location = 'location of %s is here'
    return HttpResponse('location')