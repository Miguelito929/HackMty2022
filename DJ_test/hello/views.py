import json
from hello.models import Event
import random
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt # whatsapp
from twilio.twiml.messaging_response import MessagingResponse # for Whatsapp

import time
import openai
import deepl
import googlemaps
from twilio.rest import Client


# Twilio data
account_sid = "AC8f7bff14f6c07c252fcc366f03dd1236"   # Falta getenv
auth_token = "ebcfa1942f52d48027c1795f46be45eb"      # Falta getenv
client = Client(account_sid, auth_token) 

# Openai key
openai.api_key = "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" # Falta getenv

# Deepl key
deepl_key = "104f9e4d-8f01-1494-3194-8f9d63b7a1cc:fx"

# Google maps key
maps_key = "AIzaSyDt2BpJAtrIU3S-tQ_GcU_NmUnndZadtNk"
gmaps = googlemaps.Client(key=maps_key)


def home2(request):
    return HttpResponse("Bienvenido a AI Way, tu aliado en mantenerte seguro")

def home(request):

    all_entries = Event.objects.all()
    print("$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", [(entry.category, entry.location, entry.description) for entry in all_entries])

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

# def funcion_todo(message):

# Function that reads the last message
def read_message() -> str:
    message = client.messages.list()
    print(message.body)
    return message.body


# Function that checks whether the response is complete
def is_none(response: str) -> bool:
    lst_response = response.split("|")
    return "None" == lst_response[3]


# Function that translates the message
def translate_message(message: str) -> str:
    translator = deepl.Translator(deepl_key)
    result = translator.translate_text(message, target_lang="EN-US")
    return result.text


# Function that if the location is not None, it sends a message
def ask_location(user):
    client.messages.create(from_="whatsapp:+14155238886",
                        body="¿Donde ocurrio el evento?",
                        to=user)
    # time.sleep(10)
    # while message() == "¿Donde ocurrio el evento?":
    #     time.sleep(10)
    return read_message()


# Function that recognize the important aspects of an alert
def recognize_alert(message, user):
    # message = message()
    message = translate_message(message)
    print(message)
    table = "|Traffic or Security or None|Event|Location or None|\n|:---:|:---:|:---:|"    # Temporal
    response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"A table that parse the following alert if it applies\n{message}\n{table}\n",
            temperature=0.03,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    response = response.choices[0].text
    # None in response?
    if is_none(response):
        location = ask_location(user)
        location = translate_message(location)
        response = response.replace("None", location)
    
    # Prints the response
    print(response)

    return response


@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    # data_client = client.messages.list(limit=1, )[0]
    # msg_id = request.POST.get('MessageSid')
    
    # print(request.POST)
    # print(date_created) # when was the message forwarded
    print(f'{user} says {message}')

    resp = recognize_alert(f'{message}', user)

    print( "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" , resp.split("|"))

    response = MessagingResponse()
    response.message('¡Ay Wey! Gracias por reportar.')

    cat, desc, loc = [x for x in resp.split("|") if x]
    geocode = gmaps.geocode(loc)
    lat = geocode[0]["geometry"]["location"]["lat"]
    lng = geocode[0]["geometry"]["location"]["lng"]
    event = Event(category=cat, latitude=lat, longitude=lng, description=desc)
    event.save()


    return HttpResponse(str(response))