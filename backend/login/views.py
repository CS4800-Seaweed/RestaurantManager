from django.shortcuts import render
from database.models import Restaurants, Restaurant, Worker

# Create your views here.
def login_view(request):
    if request.method == "POST":
        #get input from page
        username = request.POST.get("username")
        password = request.POST.get("password")

        worker = Worker.objects.filter(username=username)
        if len(worker) == 1:
            if password == worker[0].user_password:
                #TODO: user should be logged in, return instrument panel page
                pass
            else:
                #TODO: return page with alteration (notify user of incorrect password)
                pass
        elif len(worker) > 1:
            print("ERROR OUR WORKER PASSWORD IS NOT UNIQUE, WE WOO WE WOO")
        else:
            #return page with alteration (notify user of incorrect username, prompt to create account)
            pass
    return render(request, 'login/login.html')