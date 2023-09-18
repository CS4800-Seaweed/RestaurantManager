from django.urls import path

from . import views

urlpatterns = [
    path("anthony", views.AnthHello, name="anthony's hello world"),
    path("joseph", views.JoHello, name="Joseph's spice girls")
]