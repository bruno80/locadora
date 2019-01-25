from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('automovel/', views.automovel_list),
    path('automovel/<int:veiculo_id>/', views.automovel_show),
]