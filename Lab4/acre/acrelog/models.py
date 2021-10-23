from django.db import models
from django.db.models import fields

# Create your models here.

# those will be the drop down list to choose field type with different types

FIELD_TYPE = [
    ('research', 'Research'),
    ('commercial', 'Commercial'),
]

CURRENT_STATE = [
    ('used', 'Used'),
    ('not used', 'Not Used'),
]

WORKER_TYPE = [
    ('technician', 'Technician'),
    ('researcher', 'Researcher'),
    ('student', 'Student'),
    ('manager', 'Manager'),
]

JOB_TYPE = [
    ('research job', 'Research Job'),
    ('commercial job', 'Commercial Job'),
    ('class practice', 'Class Practice'),
]


# Class are here three class, worker, field and job

class Field(models.Model):
    field_type = models.CharField(choices=FIELD_TYPE, max_length=100)
    current_state = models.CharField(choices=CURRENT_STATE, max_length=64)
    field_name = models.CharField(max_length=200)

    def __str__(self):
        return self.field_name


class Worker(models.Model):
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    worker_type = models.CharField(choices=WORKER_TYPE, max_length=64)
    
    def __str__(self):
        return str((self.FirstName) + ' ' + self.LastName)

class Job(models.Model):

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='jobs')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='job_done')
    job_title = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    job_date = models.DateTimeField()
    material_used = models.CharField(max_length=100)
    material_amount = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPE, max_length=100)

    def __str__(self):
        return self.job_title




