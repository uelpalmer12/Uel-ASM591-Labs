from django.db import models 


# Create your models here.

OBSERVATION_TYPES = [
  ('weather', 'Weather'), 
  ('crop', 'Crop'), 
  ('soil', 'Soil'), 
  ('water', 'Water'), 
  ('pest', 'Pest'), 
  ('other', 'Other'),
]



class Field (models.Model):
    field_name= models.CharField(max_length=200)
    date_planted = models.DateTimeField()

    def __str__(self): #this is the function declaration
     return self.field_name #and this will return the field name attribute


    



class Observation(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    observation_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    observation_content = models.CharField(max_length=100)
    observation_type = models.CharField(choices=OBSERVATION_TYPES, max_length=100)
    observation_date = models.DateTimeField()

    def __str__(self):
     return self.observation_title


    
