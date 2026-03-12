from django.shortcuts import render,redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Livro, Sinopse, Opiniao
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib import messages



def cadastro_livro(request): #HTML #submit book

    mensagem = ''

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get ('autor')
        ano_publicacao = request.POST.get ('ano_publicacao')
        editora = request.POST.get ('editora')
        imagem = request.FILES.get ('imagem')

        if Livro.objects.filter(titulo=titulo, autor=autor, editora=editora).exists(): #verify if the book already exists
            mensagem = 'Este livro já foi adicionado!'
        else:
            Livro.objects.create(
                titulo=titulo,
                autor=autor,
                ano_publicacao=ano_publicacao,
                editora=editora,
                imagem=imagem
            )
            return redirect('lista_livros')
        
    return render(request, 'livros/cadastro_livro.html', {'mensagem': mensagem})

#function to list book data
def lista_livros(request): #HTML
    livros = Livro.objects.all().order_by('-criado_em')
    return render(request, 'livros/listar.html', {'livros':livros})

#function to show book detail
def detalhes_livro(request, slug):
    livro = get_object_or_404(Livro, slug=slug ) 
    
    if request.method == "POST":
        conteudo = request.POST.get('conteudo')
        if conteudo:
            Sinopse.objects.create(livro=livro, conteudo=conteudo, autor = request.user )
            return redirect('detalhes_livro', slug=slug)
        
    sinopses=livro.sinopses.all().order_by('-criado_em')
    return render(request, 'livros/detalhes.html', {'livro':livro, 'sinopses':sinopses})

def opiniao_livro(request, slug):
    livro = get_object_or_404(Livro, slug=slug)

    if request.method == "POST":
        conteudo = request.POST.get('conteudo')
        if conteudo:
            Opiniao.objects.create(livro=livro, conteudo=conteudo, autor = request.user)
            return redirect(opiniao_livro, slug=slug)
        
    opinions=livro.opinions.all().order_by('-criado_em')
    return render(request, 'livros/opiniao.html', {'livro':livro, 'opinions':opinions})

def contato(request):
    return render(request, 'livros/contato.html')

def add_capa(request, slug):
    livro = get_object_or_404(Livro, slug=slug)
    
    if request.method == 'POST':
        imagem=request.FILES.get ('imagem')

        if imagem:
            livro.imagem = imagem
            livro.save()
            return redirect(detalhes_livro, slug=slug)

    return render (request, 'livros/add_capa.html',{'livro':livro})

        
            

#---------------------------------------------------------------------------------------------------------------
