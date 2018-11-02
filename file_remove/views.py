from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import remove
from server.vars import PATH, SITE

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    curr = request.GET['delete']
    curr = curr.split('/')
    curr = curr[:-1]
    fold = ''
    for elem in curr:
        fold += elem + '/'
    current_site = SITE + fold.replace(PATH, '')
    remove(request.GET['delete'])
    remove(PATH + 'static/' + request.GET['delete'].replace(PATH, ''))
    return HttpResponseRedirect(current_site.replace(' ', '%20'))