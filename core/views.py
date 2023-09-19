from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from core.models import Clientes
from core.forms import ClienteForm


# Create your views here.

def login_page(request):
    if request.method == "GET":
        return render(request, 'main/login.html', {})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "USUÁRIO OU SENHA INVÁLIDO") 
    return redirect('/')

def registrar_page(request):
    if request.method == 'GET':
        return render(request, 'main/registrar.html',)
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username).first()

        if user:
            messages.info(request, "USUÁRIO JÁ EXISTE") 
            return redirect('/registrar')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse("Usuário Cadastrado")
    
@login_required(login_url='/login')
def index_page(request):
    clientes = Clientes.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'main/main.html', context)

@login_required(login_url='/login')
def cliente_add(request):
    form = ClienteForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'main/cliente_add.html', context)

@login_required(login_url='/login')
def cliente_edit(request, cliente_pk):
    cliente = Clientes.objects.get(pk=cliente_pk)

    form = ClienteForm(request.POST or None, instance=cliente)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        'form': form
    }

    return render(request, 'main/cliente_edit.html', context)

def cliente_delete(request, cliente_pk):
    cliente = Clientes.objects.get(pk=cliente_pk)
    cliente.delete()

    return redirect('/')


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')