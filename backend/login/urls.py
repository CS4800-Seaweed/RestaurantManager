from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('mainmenu/', views.mainmenu_view, name='mainmenu_view'),
]
