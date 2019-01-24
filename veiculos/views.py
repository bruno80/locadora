from django.shortcuts import render
from django.http import HttpResponse
from . models import Veiculo

def home(request):
      return render(request, 'home.html', {})

def automovel_list(request):
      veiculos = Veiculo.objects.all()
      return render(request, 'automovel/list.html', {'veiculos':veiculos})