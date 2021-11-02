from django.contrib import admin

from .models import Worker, Field, Job
# Register your models here.


admin.site.register(Worker)
admin.site.register(Field)
admin.site.register(Job)