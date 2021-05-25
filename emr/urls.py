from django.urls import path
from . import views


app_name = 'emr'  # here for namespacing of urls.

urlpatterns = [
    path("", views.index, name="index"),
]