from django.urls import path

from . import views

urlpatterns = [
    path("", views.AnthHello, name="anthony's hello world"),
]