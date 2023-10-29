from django.shortcuts import render, redirect
from .models import Ingredient, RestockRecord
from .forms import RestockForm

#TODO: ENSURE URLS ARE WORKING AS INTENDED

#TODO: MAKE THIS WORK WITH THE NEW DATABASE SCHEMA
#TODO: SEPARATE INGREDIENTS AND SUPPLIES (not important rn)
def view_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients.html', {'ingredients': ingredients})

#TODO: MAKE THIS WORK WITH NEW DATABASE SCHEMA
def restock_ingredient(request):
    if request.method == "POST":
        form = RestockForm(request.POST)
        if form.is_valid():
            restock_record = form.save()
            ingredient = restock_record.ingredient
            ingredient.quantity += restock_record.added_quantity
            ingredient.save()
            return redirect('view_ingredients')
    else:
        form = RestockForm()
    return render(request, 'restock.html', {'form': form})

