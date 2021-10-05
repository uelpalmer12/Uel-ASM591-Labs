from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Field
# Create your views here.
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)

def notes(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    return render(request, 'farmnotes/notes.html', {'field': field})

def observation(request, field_id, observation_id):
        return HttpResponse("You are looking at observation %s related to field %s"(observation_id, field_id))