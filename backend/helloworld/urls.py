from django.urls import path

from . import views

urlpatterns = [
    path("anthony", views.AnthHello, name="anthony's hello world"),
    path("joseph", views.JoHello, name="Joseph's spice girls"),
    path("Kennedy", views.KenHello, name="kennedy's ken song"),
    path('kennedyA4', views.KenA4, name='scrape'),
]