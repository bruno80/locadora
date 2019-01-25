from django.shortcuts import render
from django.http import HttpResponse
from . models import Veiculo

def home(request):
      return render(request, 'home.html', {})

def automovel_list(request):
      veiculos = Veiculo.objects.all()
      return render(request, 'automovel/list.html', {'veiculos':veiculos})

def automovel_show(request, veiculo_id):
      veiculo = Veiculo.objects.get(pk=veiculo_id)
      return render(request, 'automovel/show.html', {'veiculo':veiculo})