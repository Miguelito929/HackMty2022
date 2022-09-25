import json
import random
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
            'someDjangoVariable' : json.dumps([{'lat': 25.6787278+random.random()*0.1, 
                                                'lng': -100.2899258+random.random()*0.1}
                                                for _ in range(25)])
        }
    )