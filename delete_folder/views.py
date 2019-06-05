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
    ans += '<style> th {border: transparent; vertical-align: middle; ' \
           'font-size: 80; font-family: Calibri; height: 50%; width: 100%;} </style>'
    ans += '<style> td {border: transparent;' \
           'font-size: 200; font-family: Calibri; width=50%; height: 50%;' \
           'vertical-align: middle; text-align: center;} </style>'
    ans += '<style> table {border: transparent; margin: auto; ' \
           'text-align: center; background-color: #ffffff; ' \
           'height: 100%; width: 100%} </style>'
    ans += '<style> a { text-decoration: none; } </style>'
    ans += '<style type="text/css"> A { color: #a55ac4; }' \
           ' A:visited { color: #a55ac4; } </style>'
    ans += "<style> @font-face { font-family: Calibri; src: url(%s); } " \
           "h1 { font-family: Calibri; } </style>" % FONT_PATH
    ans += "</head>"
    ans += '<body style="background: #fff">'
    ans += "<table><tr><th colspan='2'><a style='color: #b721ff'>" \
           "Вы уверены, что хотите удалить папку %s со всем ее содержимым?" \
           "</a></th></tr>" % ('"' + file + '"')
    ans += "<tr><td><a href=%s>Да</a></td>" \
           "<td><a href=%s>Нет</a></td></tr></table>" \
           % (delete.replace(' ', '%20'), current_site.replace(' ', '%20'))
    ans += "</body>"
    return HttpResponse(ans)