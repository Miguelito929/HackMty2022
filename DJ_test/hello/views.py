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
            'someDjangoVariable' : json.dumps([{'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 },
            {'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 },
            {'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 },
            {'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 },
            {'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 },
            {'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 },
            {'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 },
            {'lat': 25.6787278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.687278+random.randrange(1,10)*.01, 'lng': -100.289258+random.randrange(1,10)*.01 }, 
            {'lat': 25.617278+random.randrange(1,10)*.01, 'lng': -100.2859258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6487278+random.randrange(1,10)*.01, 'lng': -100.2899258+random.randrange(1,10)*.01 }, 
            {'lat': 25.6527278+random.randrange(1,10)*.01, 'lng': -100.2868258+random.randrange(1,10)*.01 }, 
            {'lat': 25.651278+random.randrange(1,10)*.01, 'lng': -100.279258+random.randrange(1,10)*.01 }])
        }
    )