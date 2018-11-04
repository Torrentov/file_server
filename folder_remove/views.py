from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import remove
from shutil import rmtree
from server.vars import PATH, SITE

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    curr = request.GET['delete']
    curr = curr.split('/')
    curr = curr[:-2]
    fold = ''
    for elem in curr:
        fold += elem + '/'
    current_site = SITE + fold.replace(PATH + 'static/', '')
    rmtree(PATH + request.GET['delete'].replace(PATH, ''),
           ignore_errors=False, onerror=None)
    return HttpResponseRedirect(current_site.replace(' ', '%20'))