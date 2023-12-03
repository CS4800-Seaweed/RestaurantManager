from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='supply_index'),
    path('<int:supply_id>/', views.detail, name='supply_detail'),
    path('restock/', views.restock_ingredient, name='restock_ingredient'),
    path('restock/<int:supply_id>/', views.restock_specific, name='restock_specific'),
    path('search_menu/', views.search_ingredient, name='search_supply'),
    path('add/', views.addSupply, name='add_supply')
]
