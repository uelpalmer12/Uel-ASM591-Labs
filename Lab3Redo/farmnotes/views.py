from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world! You're at the farmnotes index, or 'home' page.")

def notes (request, field_id):
    return HttpResponse("You are looking at the notes related to field %s." % field_id)

def observation(request, field_id, observation_id):
        return HttpResponse("You are looking at observation %s related to field %s"(observation_id, field_id))