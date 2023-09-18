from django.shortcuts import render, HttpResponse

# Create your views here.
def AnthHello(request):
    return HttpResponse(
        '"Our name has nothing to do with the food" \n'  
        '- Seaweed')
