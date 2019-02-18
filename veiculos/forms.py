from django.forms import ModelForm, TextInput
from .models import Veiculo

class VeiculoForm(ModelForm):
      class Meta:
            model = Veiculo
            fields = '__all__'
            widjets = {
                  'tipo': TextInput(attrs={'class':'form-control'}),
                  'nome': TextInput(attrs={'class':'form-control'}),
                  'ano': TextInput(attrs={'class':'form-control'}),
                  'fabricante': TextInput(attrs={'class':'form-control'})
            }