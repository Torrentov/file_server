from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from server.vars import SITE

# Create your views here.

def get_passw(request):
    if request.user.is_authenticated and request.session['auth'] == 1:
        return HttpResponseRedirect(SITE + 'needed_files/')
    error = ''
    user = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
                login(request, user)
                request.session['auth'] = 1
                return HttpResponseRedirect("files?folder=needed_files/")
        else:
            error = "Ваши логин и пароль не совпадают\nПожалуйста, попробуйте снова"
    return render(request, "passw.html", {'error': error})