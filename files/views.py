from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from time import time
import os
from server.vars import SITE_UPLOAD, SITE_DELETE_FOLDER, SITE_DELETE_FILE,\
    SITE_CREATE_FOLDER, FILE_PATH, SERVER_PATH, SITE, PATH, FONT_PATH

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    folder = request.GET['folder']
    real_path = PATH + "static/" + folder
    raw_current = os.listdir(path=real_path)
    ans = '<head><title>Файлы</title>'
    ans += '<style> a { text-decoration: none; } </style>'
    ans += '<style type="text/css"> A { color: #8b4513; } A:visited { color: #8b4513; } </style>'
    ans += '<style> @font-face { font-family: Calibri; src: url(%s); } h1 { font-family:' \
           'Calibri; } </style>' % FONT_PATH
    ans += '</head>\n'
    ans += '<body style="background: beige">'
    ans += '{% load staticfiles %}\n'
    ans += "<a href='" + SITE_CREATE_FOLDER + "?folder=" + real_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
           "<img src='{% static 'images/create_folder.png' %}'" \
           " alt='Создать папку' title='Создать папку' width=70 height=70></a>\n"
    ans += "&#160;&#160;&#160;&#160;&#160;"
    ans += "<a href='" + SITE_UPLOAD + "?folder=" + folder.replace(' ', '%20') + "' style='color: #2a5c03'> " \
           "<img src='{% static 'images/upload_file.png' %}'" \
           " alt='Загрузить файл' title='Загрузить файл' width=70 height=70></a>\n"
    if folder != 'needed_files/':
        ans += "&#160;&#160;&#160;&#160;&#160;"
        ans += "<a href='" + SITE_DELETE_FOLDER + "?delete=" + real_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
            "<img src='{% static 'images/trash_bin.png' %}'" \
            " alt='Удалить папку' title='Удалить папку' width=70 height=70></a>\n"
    ans += "</br></br></br></br></br>"
    if folder != 'needed_files/':
        curr = folder.split('/')[:-2]
        fold = ''
        for elem in curr:
            fold += elem + '/'
        ans += "<a href=" + SITE + fold.replace(' ', '%20') + " style='color: #2a5c03'>" \
            "<img src='{% static 'images/back_icon.png' %}' alt='Назад' title='Назад' height=70 width=70></a>\n"
    current = []
    logs = open(SERVER_PATH + "/server/logs.txt", "r")
    time_base = dict()
    for line in logs:
        line = line.split()
        time_base[line[0].replace(PATH + 'static/', '')] = line[1]
    logs.close()
    for elem in raw_current:
        current.append([elem, 0, real_path])
    while len(current) != 0:
        elem = current[0]
        if os.path.isdir(elem[2] + elem[0]):
            current_path = elem[2] + elem[0] + '/'
            curr = current_path.replace(FILE_PATH, '')
            ans += '<h1><img src="{% static "images/folder_icon.png" %}"' \
                   ' alt="Папка" height="50" width="50" />&#160;&#160;' +\
                "<a href='/files?folder=needed_files" +\
                curr.replace(' ', '%20') + "'><font face='Calibri'>" + elem[0] + "</font></a>" + \
                "<input type='hidden' class='zalupa' name=" + elem[0].replace(' ', '%20') + " value=" +\
                   time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                   "></h1>\n"
        else:
            current_file = elem[2] + elem[0]
            current_file = current_file.replace(PATH + 'static/', '')
            ans += "<h1><img src=" + '"' + '{% static ' + '"images/file_icon.png"' + ' %}' + '"' + " height='50' width='40' alt='Файл'/>&#160;&#160;" +\
                "<a href='" + '{% static "' + request.GET['folder'] + elem[0] + '" %}' + "'" +\
                " download><font face='Calibri'>" + "" + elem[
                0] + "</font></a>&#160;&#160;<a href='" + SITE_DELETE_FILE + "?delete=" + \
                current_file.replace(' ', '%20') + "' style='color: #2a5c03'>" + \
                "<img src='{% static 'images/trash_bin.png' %}' alt='Удалить файл' title='Удалить файл' height=30 width=30></a>" \
                + "<input type='hidden' class='zalupa' name=" + elem[0].replace(' ', '%20') + " value=" +\
                time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                "></h1>\n"
        current.pop(0)
    ans += '</body>'
    file = open(SERVER_PATH + "/files/templates/site.html", "w")
    print(ans, file=file)
    file.close()
    return render(request, "site.html")