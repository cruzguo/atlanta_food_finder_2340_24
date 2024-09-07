from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Restaurant
# Create your views here.

#the display for details about each restaurant
def rest_info(request, name):
    restaurant = get_object_or_404(Restaurant, pk=name)

    return HttpResponse("hello")