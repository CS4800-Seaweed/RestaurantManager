from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, Supply
from .forms import RestockForm

#TODO: ENSURE URLS ARE WORKING AS INTENDED

#TODO: MAKE THIS WORK WITH THE NEW DATABASE SCHEMA
#TODO: SEPARATE INGREDIENTS AND SUPPLIES (not important rn)
def index(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'stock/supplies.html', {'ingredients': ingredients})

def detail(request, supply_id):
    supply = get_object_or_404(Supply, pk=supply_id)
    return render(request, 'stock/detail.html', {'supply': supply})

#TODO: MAKE THIS WORK WITH NEW DATABASE SCHEMA
def restock_ingredient(request):
    if request.method == "POST":
        form = RestockForm(request.POST)
        if form.is_valid():
            restock_record = form.save()
            ingredient = restock_record.ingredient
            ingredient.quantity += restock_record.added_quantity
            ingredient.save()
            return redirect('supply_index')
    else:
        form = RestockForm()
    return render(request, 'stock/restock.html', {'form': form})

