from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='supply_index'),
    path('<int:supply_id>', views.detail, name='supply_detail'),
    path('restock/', views.restock_ingredient, name='restock_ingredient'),
]
