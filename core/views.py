from django.shortcuts import render, redirect
from .models import Hamburguer
from .forms import ClienteForm

def home(request):
    hamburgueres = Hamburguer.objects.all()
    return render(request, 'core/index.html', {'hamburgueres': hamburgueres})

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print("Usuário salvo com sucesso!")
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'core/cadastro.html', {'form': form})