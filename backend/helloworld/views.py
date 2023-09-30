from django.shortcuts import render, HttpResponse
#Imports for kennedy's library
from django.http import HttpResponse
from bs4 import BeautifulSoup
#import requests

# Create your views here.
def AnthHello(request):
    return HttpResponse(
        '"Our name has nothing to do with the food" \n'  
        '- Seaweed')

def JoHello(request):
    return HttpResponse("the spice girls")

def KenHello(request):
    return HttpResponse("Im just Ken, everywhere else id be a ten")

#Kennedy's assignment 4 library method
def KenA4(request):
    url = 'https://kennedyjanto2.github.io/KennedyJanto/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = []
    for a in soup.find_all('a', href=True):
        links.append(a['href'])
    
    return HttpResponse(', '.join(links))