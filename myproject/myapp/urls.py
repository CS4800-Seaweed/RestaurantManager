from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple_api),
]
