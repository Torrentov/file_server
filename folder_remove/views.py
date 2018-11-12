from django.shortcuts import render
from django.http import HttpResponseRedirect
from os import remove
from shutil import rmtree
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
    curr = curr[:-2]
    fold = ''
    for elem in curr:
        fold += elem + '/'
    current_site = SITE + fold.replace(PATH + 'static/', '')
    rmtree(PATH + request.GET['delete'].replace(PATH, ''),
           ignore_errors=False, onerror=None)
    remove = []
    for key in base:
        if key.count((PATH + request.GET['delete'].replace(PATH, '')).replace(' ', '%20')[:-1]) > 0:
            remove.append(key)
    for key in remove:
        del base[key]
    for key in base:
        print(key, base[key], file=log)
    log.close()
    return HttpResponseRedirect(current_site.replace(' ', '%20'))