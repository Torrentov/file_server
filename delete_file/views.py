from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from server.vars import PATH, FILE_DELETE, SITE

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    delete = FILE_DELETE + request.GET['delete'].replace(' ', '%20')
    curr = request.GET['delete']
    curr = curr.split('/')
    curr = curr[:-1]
    fold = ''
    for elem in curr:
        fold += elem + '/'
    current_site = SITE + fold.replace(PATH, '')
    file = request.GET['delete'].split('/')[-1]
    ans = "<head><title>Удалить файл</title></head>"
    ans += "<h1>Вы уверены, что хотите удалить файл %s?" % file
    ans += "<h1><a href=%s>Да</a></h1>" % delete.replace(' ', '%20')
    ans += "</br></br>"
    ans += "<h1><a href=%s>Нет</a></h1>" % current_site.replace(' ', '%20')
    return HttpResponse(ans)