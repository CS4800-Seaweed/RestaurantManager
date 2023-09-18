from django.shortcuts import render, HttpResponse

# Create your views here.
def AnthHello(request):
    return HttpResponse(
        '"Our name has nothing to do with the food" \n'  
        '- Seaweed')

def JoHello(request):
    return HttpResponse("the spice girls")

def KenHello(request):
    return HttpResponse("Im just Ken, everywhere else id be a ten")