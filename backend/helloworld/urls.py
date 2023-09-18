from django.urls import path

from . import views

urlpatterns = [
    path("anthony", views.AnthHello, name="anthony's hello world"),
]