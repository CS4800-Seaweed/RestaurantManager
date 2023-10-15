from django.urls import path
from . import views

urlpatterns = [
    #TODO: ADD VIEWING OF A SINGULAR INGREDIENT
    path('ingredients/', views.view_ingredients, name='view_ingredients'),
    path('restock/', views.restock_ingredient, name='restock_ingredient'),
]
