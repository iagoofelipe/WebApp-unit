from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "GET":
        return render(request, 'index.html', {})
    elif request.method == "POST":
        return HttpResponse("tela de requisição")