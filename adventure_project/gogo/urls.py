from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first, name="first"),
    path('second/', views.second, name="second"),
    path('third/', views. thrid, name="third"),
    path('firth/' , views.firth, name="firth"),

    
    ]