from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from server.vars import PATH, FOLDER_DELETE, SITE, FONT_PATH

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    delete = FOLDER_DELETE + request.GET['delete'].replace(' ', '%20')
    curr = request.GET['delete']
    curr = curr.split('/')
    curr = curr[:-1]
    fold = ''
    for elem in curr:
        fold += elem + '/'
    current_site = SITE + fold.replace(PATH + 'static/', '')
    file = request.GET['delete'].split('/')[-2]
    ans = "<head><title>Удалить папку</title>"
    ans += '<style> a { text-decoration: none; } </style>'
    ans += '<style type="text/css"> A { color: #2a5c03; } A:visited { color: #2a5c03; } </style>'
    ans += "<style> @font-face { font-family: Calibri; src: url(%s); } h1 { font-family:' \
           'Calibri; } </style>" % FONT_PATH
    ans += "</head>"
    ans += '<body style="background: beige">'
    ans += "<h1><font face='Calibri'><a style='color: #8b4513'>" \
           "Вы уверены, что хотите удалить папку %s со всем ее содержимым?" \
           "</br></br></a></font></h1>" % ('"' + file + '"')
    ans += "<h1><font face='Calibri'><a href=%s>Да</a>&#160;&#160;&#160;&#160;&#160;" \
           "&#160;&#160;&#160;&#160;&#160;<a href=%s>Нет</a></font></h1>" \
           % (delete.replace(' ', '%20'), current_site.replace(' ', '%20'))
    ans += "</body>"
    return HttpResponse(ans)