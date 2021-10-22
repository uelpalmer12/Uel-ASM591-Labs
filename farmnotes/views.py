from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Field, Observation
# Create your views here.
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)

def notes(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'farmnotes/notes.html', {'field': field})

def observation(request, observation_id, field_id):
    observation = get_object_or_404(Observation,pk=observation_id)
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'farmnotes/observations.html', {'observation': observation, 'field': field})


