from django.shortcuts import render

def home(request):
      return render(request, 'home.html', {})

def carro_list(request):
      return render(request, 'carro/list.html', {})