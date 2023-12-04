from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Company, Worker
from django.contrib.auth import get_user_model
import re


# Create your views here.
def login_view(request):
    print("login")
    context = {}
    
    if request.method == "POST":
        #get input from page
        username = request.POST.get("username")
        password = request.POST.get("password")

        worker = authenticate(request, username=username, password=password)
        print("worker:", worker)
        if worker is not None:
            login(request, worker)
            return redirect('stock:search_supply')
            pass
        else:
            context['login_failed'] = True
    return render(request, 'login/login.html', context)

def register_view(request):
    companies = Company.objects.all()
    company = None
    if not companies.exists():
        #create company if no company exists
        new_company = Company(name="centerpointe")
        new_company.save()
        print("no company")
    else:
        company = companies[0]

    print("register")
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmpass = request.POST.get("confirmpass")

        Workers = get_user_model()

        if password == confirmpass and not Worker.objects.filter(username=username).exists() and not Worker.objects.filter(email=email).exists():
            Workers.objects.create_user(username=username, restaurant=company, first_name=firstname, last_name=lastname, email=email, password=confirmpass)
            return redirect('login:login_view')
    return render(request, 'login/register.html')

def mainmenu_view(request):
    return render(request, 'login/mainmenu.html')

#checker for valid email format
def isvalidEmail(email):
    pattern = "^\S+@\S+\.\S+$"
    objs = re.search(pattern, email)
    try:
        if objs.string == email:
            return True
    except:
        return False