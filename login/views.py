from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Login

def validate_login(request):
    user_login = request.POST.get('user')
    password = request.POST.get('password')

    user = Login.objects.filter(user_login=user_login)
    if len(user) > 0:
        authorized = user[0].password == password
        user_name = user[0].name if authorized else ''
        # return HttpResponse("{'authorized':'"+str(authorized)+"'user_name': '{1}'}".format(authorized, user_name))
        return HttpResponse(str({'authorized':str(authorized), 'user_name':user_name}).replace("'",'"'))
    
    return HttpResponse('{"authorized":"False"}')


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    
    elif request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        
        if '' in (user, password):
            return render(request, 'index.html')

        return validate_login(request)