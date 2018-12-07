from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from time import time
import os
from server.vars import SITE_UPLOAD, SITE_DELETE_FOLDER, SITE_DELETE_FILE,\
    SITE_CREATE_FOLDER, FILE_PATH, SERVER_PATH, SITE, PATH

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    folder = request.GET['folder']
    real_path = PATH + "static/" + folder
    raw_current = os.listdir(path=real_path)
    ans = '<head><title>Файлы</title>'
    ans += '<style> a { text-decoration: none; } </style>'
    ans += '<style type="text/css"> A { color: #0000ff; } A:visited { color: #0000ff; } </style>'
    ans += '</head>\n'
    ans += '{% load staticfiles %}\n'
    ans += "<h1><a href='%s?folder=%s' style='color: #7442c8'>**Создать папку**</a></h1>\n"  %\
    (SITE_CREATE_FOLDER, real_path.replace(' ', '%20'))
    if folder != 'needed_files/':
        ans += "<h1><a href='%s?delete=%s' style='color: #7442c8'>**Удалить папку**</a></h1>\n" %\
        (SITE_DELETE_FOLDER, real_path.replace(' ', '%20'))
    ans += "<h1><a href='%s?folder=%s' style='color: #7442c8'>**Загрузить файл**</a></h1></br>\n" % \
    (SITE_UPLOAD, folder.replace(' ', '%20'))
    if folder != 'needed_files/':
        curr = folder.split('/')[:-2]
        fold = ''
        for elem in curr:
            fold += elem + '/'
        ans += "<h1><a href=" + SITE + fold.replace(' ', '%20') + ">**Назад**</a></h1>\n"
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
                   ' alt="Папка" height="50" width="50" />' +\
                "<a href='/files?folder=needed_files" +\
                curr.replace(' ', '%20') + "'>" + elem[0] + "</a>" + \
                "<input type='hidden' name=" + elem[0].replace(' ', '%20') + " value=" +\
                   time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                   "></h1>\n"
        else:
            current_file = elem[2] + elem[0]
            current_file = current_file.replace(PATH + 'static/', '')
            ans += "<h1><img src=" + '"' + '{% static ' + '"images/file_icon.png"' + ' %}' + '"' + " height='50' width='40' alt='Файл'/>" +\
                "<a href='" + '{% static "' + request.GET['folder'] + elem[0] + '" %}' + "'" +\
                " download>" + "" + elem[
                0] + "</a>&#160;&#160;&#160;&#160;&#160;<a href='" + SITE_DELETE_FILE + "?delete=" + \
                current_file.replace(' ', '%20') + "' style='color: #7442c8'>**Удалить файл**</a>" \
                + "<input type='hidden' name=" + elem[0].replace(' ', '%20') + " value=" +\
                time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                "></h1>\n"
        current.pop(0)
    file = open(SERVER_PATH + "/files/templates/site.html", "w")
    print(ans, file=file)
    file.close()
    return render(request, "site.html")