from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('carro/', views.carro_list)
]