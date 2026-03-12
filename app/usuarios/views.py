from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


#Sign_in interface
def cadastro_usuario(request):
    mensagem = ''

    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if confirmar_senha != password:
            mensagem = 'As senhas nao coincidem!'
            return render(request, 'cadastro.html', {'mensagem': mensagem})
        
        if User.objects.filter(username=username).exists():
            mensagem = 'Esse nome de usuário ja existe'
            return render(request, 'cadastro.html', {'mensagem': mensagem})
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        mensagem = 'Usuario criado com sucesso!'
        return redirect('login')
    else:
         return render(request, 'cadastro.html', {'mensagem': mensagem})


#Login interface
def login_usuario(request):
    mensagem = ''
    
    if request.method == 'POST':
        username =request.POST.get('usuario')
        password = request.POST.get('senha')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_livros')
        else:
            mensagem = 'Usuario ou senha incorretos'
            return render(request, 'login.html', {'mensagem':mensagem})
    else:
        return render(request, 'login.html', {'mensagem':mensagem})
    
    
        
