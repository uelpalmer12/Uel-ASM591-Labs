from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Field, Job
# Create your views here.

def index(request):
  return render(request, 'acrelog/index.html', {
    "fields": Field.objects.all()
  })


def notes(request, field_id):
  field = get_object_or_404(Field, pk=field_id)
  return render(request, 'acrelog/notes.html', {'field': field, "jobs_done": field.job_done.all()})

def job(request, job_id, field_id):
  jobs = get_object_or_404(Job,pk=job_id)
  field = get_object_or_404(Field, pk=field_id)
  return render(request, 'acrelog/job.html', {'job': jobs, 'field': field})

def secretsauce(request):
  return render(request, 'acrelog/secretsauce.html')
