from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:field_id>", views.notes, name="notes"),
    path("<int:field_id>/<int:job_id>/", views.job, name='job'),
]