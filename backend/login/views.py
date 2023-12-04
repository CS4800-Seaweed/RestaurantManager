from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Company, Worker
import re


# Create your views here.
def login_view(request):
    print("login")
    context = {}
    
    if request.method == "POST":
        #get input from page
        username = request.POST.get("username")
        password = request.POST.get("password")

        worker = Worker.objects.filter(username=username)
        print("worker:", worker)
        if len(worker) == 1:
            if password == worker[0].user_password:
                return redirect('stock:search_supply')
                pass
            else:
                return render(request, 'login/login.html')
                context['login_failed'] = True
                pass
        elif len(worker) > 1:
            print("ERROR OUR WORKER PASSWORD IS NOT UNIQUE, WE WOO WE WOO")
            context['login_failed'] = True
        else:
            #return page with alteration (notify user of incorrect username, prompt to create account)
            pass
            context['login_failed'] = True
    return render(request, 'login/login.html')

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

        if password == confirmpass and not Worker.objects.filter(username=username).exists() and not Worker.objects.filter(email=email).exists():
            new_worker = Worker(username=username, restaurant=company, first_name=firstname, last_name=lastname, email=email, user_password=confirmpass)
            new_worker.save()
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