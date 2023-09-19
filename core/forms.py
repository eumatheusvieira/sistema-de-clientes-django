from core.models import Clientes
from django import forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }