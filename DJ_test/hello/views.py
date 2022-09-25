from platform import node
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime
from django.conf import settings

def home2(request):
    return HttpResponse("Bienvenido a AI Way, tu aliado en mantenerte seguro")

def home(request):
    return render(
        request,
        'hello/hello_there.html',
        {
            'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
            'someDjangoVariable': [{ "lat": 25.65, "lng": -100.298 }]
        }
    )