from django.contrib import admin

from farmnotes.models import Observation, Field

# Register your models here.

admin.site.register(Field)
admin.site.register(Observation)