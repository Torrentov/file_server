from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from time import time, ctime
import os
from server.vars import SITE_UPLOAD, SITE_DELETE_FOLDER, SITE_DELETE_FILE,\
    SITE_CREATE_FOLDER, FILE_PATH, SERVER_PATH, SITE, PATH, FONT_PATH

# Create your views here.

def ctime_to_normal(date):
    a = [date[2], date[1], date[0], date[3]]
    date = a[0] + '  ' + a[1] + ' ' + a[2] + ' ' + a[3]
    return date


def size_to_normal(size):
    if size // 1048576 >= 10:
        return str(size // 1048576) + ' МБ'
    return str(size // 1024) + ' КБ'


def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    folder = request.GET['folder']
    real_path = PATH + "static/" + folder
    raw_current = os.listdir(path=real_path)
    ans = '<head><title>Файлы</title>'
    ans += '<style> th {border: 2px solid grey; vertical-align: bottom; font-size: 40; font-family: Calibri} </style>'
    ans += '<style> td {border: 2px solid grey; vertical-align: bottom; font-size: 30; font-family: Calibri} </style>'
    ans += '<style> table {border-collapse: collapse; width: 100%; text-align: center; class: sortable} </style>'
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
    ans += "<table id='table'><tr>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=0_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=30 height=30></a>" \
           "Тип<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=0_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=30 height=30></a></th>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=1_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=30 height=30></a>" \
           "Имя файла<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=1_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=30 height=30></a></th>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=2_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=30 height=30></a>" \
           "Дата изменения<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=2_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=30 height=30></a></th>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=3_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=30 height=30></a>" \
           "Размер<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=3_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=30 height=30></a></th>" \
           "</tr>"
    for elem in raw_current:
        current.append([elem, 0, real_path])
    needed_sort = None
    try:
        needed_sort = request.GET['sorted'].split('_')
        needed_sort[0] = int(needed_sort[0])
    except:
        pass
    if needed_sort:
        page = []
        while len(current) != 0:
            elem = current[0]
            if os.path.isdir(elem[2] + elem[0]):
                current_path = elem[2] + elem[0] + '/'
                curr = current_path.replace(FILE_PATH, '')
                a = os.stat(current_path)
                date = ctime(a.st_mtime).split()[1:]
                date = ctime_to_normal(date)
                size = size_to_normal(a.st_size)
                output = '<tr><td><img src="{% static "images/folder_icon.png" %}"' \
                   ' alt="Папка" height="30" width="30" />' +\
                "</td><td><a href='/files?folder=needed_files" +\
                curr.replace(' ', '%20') + "'>" + elem[0] + "</a></td>" \
                "<td>" + date + "</td><td>" + size + "</td></tr>" + \
                "<input type='hidden' class='zalupa' name=" + elem[0].replace(' ', '%20') + " value=" +\
                   time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                   ">\n"
                page.append(['folder', elem[0], date, size, output])
            else:
                current_file = elem[2] + elem[0]
                a = os.stat(current_file)
                date = ctime(a.st_mtime).split()[1:]
                date = ctime_to_normal(date)
                size = size_to_normal(a.st_size)
                current_file = current_file.replace(PATH + 'static/', '')
                output = "<tr><td><img src=" + '"' + '{% static ' + '"images/file_icon.png"' + ' %}' + '"' + " height='30' width='24' alt='Файл'/></td>"\
                "<td><a href='" + '{% static "' + request.GET['folder'] + elem[0] + '" %}' + "'" +\
                " download>" + "" + elem[
                0] + "</a></td>" \
                     "<td>" + date + "</td>" \
                     "<td>" + size + \
                     "&#160;<a href='" + SITE_DELETE_FILE + "?delete=" + \
                current_file.replace(' ', '%20') + "' style='color: #2a5c03'>" + \
                "<img src='{% static 'images/trash_bin.png' %}' alt='Удалить файл' title='Удалить файл' height=30 width=30></a></td></tr>" \
                + "<input type='hidden' class='zalupa' name=" + elem[0].replace(' ', '%20') + " value=" +\
                time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                ">\n"
                page.append(['file', elem[0], date, size, output])
            current.pop(0)
        if needed_sort[1] == 'up':
            page.sort(key=lambda a: a[needed_sort[0]])
        else:
            page.sort(reverse=True, key=lambda a: a[needed_sort[0]])
        for elem in page:
            ans += elem[4]
        file = open(SERVER_PATH + "/files/templates/site.html", "w")
        print(ans, file=file)
        file.close()
        return render(request, "site.html")


    while len(current) != 0:
        elem = current[0]
        if os.path.isdir(elem[2] + elem[0]):
            current_path = elem[2] + elem[0] + '/'
            curr = current_path.replace(FILE_PATH, '')
            a = os.stat(current_path)
            date = ctime(a.st_mtime).split()[1:]
            date = ctime_to_normal(date)
            size = size_to_normal(a.st_size)
            ans += '<tr><td><img src="{% static "images/folder_icon.png" %}"' \
                   ' alt="Папка" height="30" width="30" />' +\
                "</td><td><a href='/files?folder=needed_files" +\
                curr.replace(' ', '%20') + "'>" + elem[0] + "</a></td>" \
                "<td>" + date + "</td><td>" + size + "</td></tr>" + \
                "<input type='hidden' class='zalupa' name=" + elem[0].replace(' ', '%20') + " value=" +\
                   time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                   ">\n"
        else:
            current_file = elem[2] + elem[0]
            a = os.stat(current_file)
            date = ctime(a.st_mtime).split()[1:]
            date = ctime_to_normal(date)
            size = size_to_normal(a.st_size)
            current_file = current_file.replace(PATH + 'static/', '')
            ans += "<tr><td><img src=" + '"' + '{% static ' + '"images/file_icon.png"' + ' %}' + '"' + " height='30' width='24' alt='Файл'/></td>"\
                "<td><a href='" + '{% static "' + request.GET['folder'] + elem[0] + '" %}' + "'" +\
                " download>" + "" + elem[
                0] + "</a></td>" \
                     "<td>" + date + "</td>" \
                     "<td>" + size + \
                     "&#160;<a href='" + SITE_DELETE_FILE + "?delete=" + \
                current_file.replace(' ', '%20') + "' style='color: #2a5c03'>" + \
                "<img src='{% static 'images/trash_bin.png' %}' alt='Удалить файл' title='Удалить файл' height=30 width=30></a></td></tr>" \
                + "<input type='hidden' class='zalupa' name=" + elem[0].replace(' ', '%20') + " value=" +\
                time_base[(request.GET['folder'] + elem[0]).replace(' ', '%20')] +\
                ">\n"
        current.pop(0)
    file = open(SERVER_PATH + "/files/templates/site.html", "w")
    print(ans, file=file)
    file.close()
    return render(request, "site.html")

# needed sort = request.GET['sorted']
# sorted = type up [0, up] files before folders
# sorted = type down [0, down] folders before files
# sorted = name up [1, up]
# sorted = name down [1, down]
# sorted = size up [3, up]
# sorted = size down [3, down]
# sorted = date up [2, up]
# sorted = date down [2, down]
# array of info about file: [type, name, date, size]