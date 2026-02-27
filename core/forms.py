from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    class Meta:
        model = Cliente
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password', 
            'telefone', 'cpf', 'cep', 'rua', 'numero', 'bairro', 'cidade', 'estado'
        ]
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'cpf': 'CPF',
        }