from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def simple_api(request):
    return JsonResponse({"message": "Hello from Django!"})
