from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import remove
from server.vars import PATH, SITE, SERVER_PATH

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    lin = open(SERVER_PATH + "/server/logs.txt", "r")
    base = dict()
    for line in lin:
        line = line.split()
        base[line[0]] = line[1]
    lin.close()
    log = open(SERVER_PATH + "/server/logs.txt", "w")
    curr = request.GET['delete']
    curr = curr.split('/')
    curr = curr[:-1]
    fold = ''
    for elem in curr:
        fold += elem + '/'
    current_site = SITE + fold.replace(PATH, '')
    remove(PATH + 'static/' + request.GET['delete'].replace(PATH, ''))
    del base[(PATH + 'static/' + request.GET['delete'].replace(PATH, '')).replace(' ', '%20')]
    for key in base:
        print(key, base[key], file=log)
    log.close()
    return HttpResponseRedirect(current_site.replace(' ', '%20'))