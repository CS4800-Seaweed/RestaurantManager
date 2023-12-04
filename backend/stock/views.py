from django.shortcuts import render, redirect, get_object_or_404
from .models import Supply
from .forms import RestockForm, SearchForm, AddForm

#TODO: ENSURE URLS ARE WORKING AS INTENDED

#TODO: MAKE THIS WORK WITH THE NEW DATABASE SCHEMA
#TODO: SEPARATE INGREDIENTS AND SUPPLIES (not important rn)
def addSupply(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_supply')
    else:
        form = AddForm()

    return render(request, 'stock/add_supply.html', {'form': form})

def deleteSupply(request, supply_id):
    supply = get_object_or_404(Supply, pk=supply_id)

    if request.method == 'POST':
        supply.delete()
        return redirect('search_supply')

    return render(request, 'stock/delete_supply.html', {'supply': supply})

def index(request):
    ingredients = Supply.objects.all()
    return render(request, 'stock/supplies.html', {'ingredients': ingredients})


def detail(request, supply_id):
    supply = get_object_or_404(Supply, pk=supply_id)
    return render(request, 'stock/detail.html', {'supply': supply})


def restock_ingredient(request):
    if request.method == "POST":
        form = RestockForm(request.POST)
        if form.is_valid():
            restock_record = form.save()
            supply = restock_record.supply
            supply.quantity += restock_record.added_quantity
            supply.save()
            return redirect('search_supply')
    else:
        form = RestockForm()
    return render(request, 'stock/restock.html', {'form': form})


def restock_specific(request, supply_id):
    if request.method == "POST":
        form = RestockForm(request.POST)
        if form.is_valid():
            restock_record = form.save()
            supply = restock_record.supply
            supply.quantity += restock_record.added_quantity
            supply.save()
            return redirect('search_supply')
    else:
        if supply_id:
            supply = get_object_or_404(Supply, pk=supply_id)
            form = RestockForm(initial={'supply': supply})
        else:
            form = RestockForm()
    return render(request, 'stock/restock.html', {'form': form})
            

def search_ingredient(request):
    form = SearchForm(request.GET)
    ingredients = Supply.objects.all()

    if form.is_valid() and form.cleaned_data['search_term']:
        search_term = form.cleaned_data['search_term']
        ingredients = Supply.objects.filter(supply_name__icontains=search_term)

    return render(request, 'stock/search_menu.html', {'form': form, 'ingredients': ingredients})

