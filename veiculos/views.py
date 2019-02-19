from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Veiculo
from .forms import VeiculoForm

def home(request):
      return render(request, 'home.html', {})

def automovel_list(request):
      veiculos = Veiculo.objects.all()
      return render(request, 'automovel/list.html', {'veiculos':veiculos})

def automovel_show(request, veiculo_id):
      veiculo = Veiculo.objects.get(pk=veiculo_id)
      return render(request, 'automovel/show.html', {'veiculo':veiculo})

def contato(request):
      return render(request, 'contato/contato.html')

def automovel_form(request):
    if (request.method == 'POST'):
        form = VeiculoForm(request.POST)
        if (form.is_valid()):
            form.save() 
            return redirect('/veiculos/automovel')          
        else:
            return render(request,'automovel/form.html', {'form':form})
    else:      
        form = VeiculoForm()
        return render(request,'automovel/form.html', {'form':form})

def automovel_edit(request, veiculo_id):
    if (request.method == 'POST'):
        veiculo = Veiculo.objects.get(pk=veiculo_id)
        form = VeiculoForm(request.POST, instance=veiculo)
        if (form.is_valid()):
            form.save()
            return redirect('/veiculos/automovel')
        else:
            return render(request,'automovel/edit.html', {'form':form, 'veiculo_id':veiculo_id})
    else:
        veiculo = Veiculo.objects.get(pk=veiculo_id)
        form = VeiculoForm(instance=veiculo)
        return render(request, 'automovel/edit.html', {'form':form, 'veiculo_id':veiculo_id})
