from django.shortcuts import render
from django.http import HttpResponse

from .models import Pessoa

def ver_produto(request):
    if request.method == "GET":
        return render(request, 'ver_produto.html', {'nome':'Iago'})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # pessoa = Pessoa(nome=nome, idade=idade)
        # pessoa.save()

        pessoas = Pessoa.objects.all()
        # return HttpResponse(pessoas[0].idade)
    
        pessoas_filtro = Pessoa.objects.filter(nome=nome)
        print(request.POST)
        return HttpResponse(pessoas_filtro.all()[0].idade)
        
    

def inserir_produto(request):
    return HttpResponse('request')