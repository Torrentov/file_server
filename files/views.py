from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from time import time, ctime
import os
from server.vars import SITE_UPLOAD, SITE_DELETE_FOLDER, SITE_DELETE_FILE,\
    SITE_CREATE_FOLDER, FILE_PATH, SERVER_PATH, \
    SITE, PATH, FONT_PATH, SITE_RENAME

# Create your views here.

def ctime_to_normal(date):
    a = [date[2], date[1], date[0], date[3]]
    date = a[0] + '  ' + a[1] + ' ' + a[2] + ' ' + a[3]
    return date


def size_to_normal(size):
    if size == '—':
        return size
    if size // 1048576 >= 10:
        return str(size // 1048576) + ' МБ'
    return str(size // 1024) + ' КБ'


def date_to_comparable(time):
    time = time.split()
    if time[2] == 'Jan':
        time[2] = '01'
    if time[2] == 'Feb':
        time[2] = '02'
    if time[2] == 'Mar':
        time[2] = '03'
    if time[2] == 'Apr':
        time[2] = '04'
    if time[2] == 'May':
        time[2] = '05'
    if time[2] == 'Jun':
        time[2] = '06'
    if time[2] == 'Jul':
        time[2] = '07'
    if time[2] == 'Aug':
        time[2] = '08'
    if time[2] == 'Sep':
        time[2] = '09'
    if time[2] == 'Oct':
        time[2] = '10'
    if time[2] == 'Nov':
        time[2] = '11'
    if time[2] == 'Dec':
        time[2] = '12'
    return (time[3] + time[2] + '%2d' + time[0]) % int(time[1])


def size_to_comparable(size):
    if size == '—':
        return 0
    size = size.split()
    if size[1] == 'МБ':
        return int(size[0]) * 1024 * 1024
    if size[1] == 'КБ':
        return int(size[0]) * 1024
    return int(size)


def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    folder = request.GET['folder']
    real_path = PATH + "static/" + folder
    raw_current = os.listdir(path=real_path)
    ans = '<head><title>Файлы</title>'
    ans += '<style> #edit {margin-top: 10px;} </style>'
    ans += '<style> #border-wrap {position: relative; padding: 1rem; background: radial-gradient(at bottom left, #21d4fd, #b721ff); padding: 10px} </style>'
    ans += '<style> th {border: 2px solid grey; border-top: transparent; border-left: transparent; border-right: transparent; vertical-align: middle; font-size: 40; font-family: Calibri} </style>'
    ans += '<style> td {padding-left: 29px; border: 2px solid grey; border-bottom: transparent; border-left: transparent; border-right: transparent; vertical-align: middle; font-size: 30; font-family: Calibri} </style>'
    ans += '<style> table {padding: 2rem; border: transparent; border-collapse: collapse; width: 100%; margin: auto; text-align: left; background-color: #ffffff} </style>'
    ans += '<style> a { text-decoration: none; } </style>'
    ans += '<style type="text/css"> A { color: #a55ac4; } A:visited { color: #a55ac4; } </style>'
    ans += '<style> @font-face { font-family: Calibri; src: url(%s); } h1 { font-family:' \
           'Calibri; } </style>' % FONT_PATH
    ans += '</head>\n'
    ans += '<body style="background: #fff">'
    ans += '{% load staticfiles %}\n'
    ans += "<a href='" + SITE_CREATE_FOLDER + "?folder=" + real_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
           "<img src='{% static 'images/create_folder.png' %}'" \
           " alt='Создать папку' title='Создать папку' width=82 height=70></a>\n"
    ans += "&#160;&#160;&#160;&#160;&#160;"
    ans += "<a href='" + SITE_UPLOAD + "?folder=" + folder.replace(' ', '%20') + "' style='color: #2a5c03'> " \
           "<img src='{% static 'images/upload_file.png' %}'" \
           " alt='Загрузить файл' title='Загрузить файл' width=86 height=70></a>\n"
    ans += "</br></br></br></br></br>"
    if folder != 'needed_files/':
        curr = folder.split('/')[:-2]
        fold = ''
        for elem in curr:
            fold += elem + '/'
        ans += "<a href=" + SITE + fold.replace(' ', '%20') + " style='color: #2a5c03'>" \
            "<img src='{% static 'images/back_icon.png' %}' alt='Назад' title='Назад' height=70 width=77></a>\n"
        ans += "&#160;"
    current = []
    logs = open(SERVER_PATH + "/server/logs.txt", "r")
    time_base = dict()
    for line in logs:
        line = line.split()
        time_base[line[0].replace(PATH + 'static/', '')] = line[1]
    logs.close()
    ans += "<div id='border-wrap'><table id='table' style={background-color: #ffffff}><tr>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=0_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=28 height=30></a>" \
           "Тип<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=0_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=28 height=30></a></th>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=1_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=28 height=30></a>" \
           "Имя файла<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=1_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=28 height=30></a></th>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=2_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=28 height=30></a>" \
           "Дата изменения<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=2_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=28 height=30></a></th>" \
           "<th><a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=3_up><img src='{% static 'images/up_arrow.png' %}' alt='Отсортировать по возрастанию' title='Отсортировать по возрастанию' width=28 height=30></a>" \
           "Размер<a href=files?folder=" + folder.replace(' ', '%20') + "&sorted=3_down><img src='{% static 'images/down_arrow.png' %}' alt='Отсортировать по убыванию' title='Отсортировать по убыванию' width=28 height=30></a></th>" \
           "<th></th></tr>"
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
                size = '—'
                output = '<tr><td><img src="{% static "images/folder_icon.png" %}"' \
                   ' alt="Папка" height="30" width="36" />' +\
                "</td><td><a href='/files?folder=needed_files" +\
                curr.replace(' ', '%20') + "'>" + elem[0] + "</a></td>" \
                "<td>" + date + "</td><td>" + size + "</td><td style='vertical-align: bottom'>" \
                "<a href='" + SITE_DELETE_FOLDER + "?delete=" + current_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
                "<img src='{% static 'images/trash_bin.png' %}'" \
                " alt='Удалить папку' title='Удалить папку' width=26 height=30></a>" \
                "<a href='" + SITE_RENAME + "?current_name=" + current_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
                "<img src='{% static 'images/rename_icon.png' %}'" \
                " alt='Переименовать' title='Переименовать' width=30 height=30></a>" \
                "</td></tr>\n"
                page.append(['folder', elem[0], date_to_comparable(date), size_to_comparable(size), output])
            else:
                current_file = elem[2] + elem[0]
                a = os.stat(current_file)
                date = ctime(a.st_mtime).split()[1:]
                date = ctime_to_normal(date)
                size = size_to_normal(a.st_size)
                rename_path = current_file.replace(' ', '%20')
                current_file = current_file.replace(PATH + 'static/', '')
                output = "<tr><td><img src=" + '"' + '{% static ' + '"images/file_icon.png"' + ' %}' + '"' + " height='30' width='24' alt='Файл'/></td>"\
                "<td><a href='" + '{% static "' + request.GET['folder'] + elem[0] + '" %}' + "'" +\
                " download>" + "" + elem[
                0] + "</a></td>" \
                     "<td>" + date + "</td>" \
                     "<td>" + size + \
                     "&#160;</td><td><a href='" + SITE_DELETE_FILE + "?delete=" + \
                current_file.replace(' ', '%20') + "' style='color: #2a5c03'>" + \
                "<img src='{% static 'images/trash_bin.png' %}' alt='Удалить файл' title='Удалить файл' height=30 width=26></a>" \
                "<a href='" + SITE_RENAME + "?current_name=" + rename_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
                "<img src='{% static 'images/rename_icon.png' %}'" \
                " alt='Переименовать' title='Переименовать' width=30 height=30></a>" \
                "</td></tr>\n"
                page.append(['file', elem[0], date_to_comparable(date), size_to_comparable(size), output])
            current.pop(0)
        if needed_sort[0] == 1:
            if needed_sort[1] == 'up':
                page.sort(key=lambda a: a[1].lower())
            else:
                page.sort(reverse=True, key=lambda a: a[1].lower())
        elif needed_sort[1] == 'up':
            page.sort(key=lambda a: a[needed_sort[0]])
        else:
            page.sort(reverse=True, key=lambda a: a[needed_sort[0]])
        for elem in page:
            ans += elem[4]
        ans += "</table></div></body>"
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
            size = '—'
            ans += '<tr><td><img src="{% static "images/folder_icon.png" %}"' \
                   ' alt="Папка" height="30" width="36" />' +\
                "</td><td><a href='/files?folder=needed_files" +\
                curr.replace(' ', '%20') + "'>" + elem[0] + "</a></td>" \
                "<td>" + date + "</td><td>" + size + "</td><td><div id='edit'>" \
                "<a href='" + SITE_DELETE_FOLDER + "?delete=" + current_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
                "<img src='{% static 'images/trash_bin.png' %}'" \
                " alt='Удалить папку' title='Удалить папку' width=26 height=30></a>" \
                "<a href='" + SITE_RENAME + "?current_name=" + current_path.replace(' ', '%20') + "' style='color: #2a5c03'> " \
                "<img src='{% static 'images/rename_icon.png' %}'" \
                " alt='Переименовать' title='Переименовать' width=30 height=30></a>" \
                "</div></td></tr>\n"
        else:
            current_file = elem[2] + elem[0]
            a = os.stat(current_file)
            date = ctime(a.st_mtime).split()[1:]
            date = ctime_to_normal(date)
            size = size_to_normal(a.st_size)
            rename_path = current_file.replace(' ', '%20')
            current_file = current_file.replace(PATH + 'static/', '')
            ans += "<tr><td><img src=" + '"' + '{% static ' + '"images/file_icon.png"' + ' %}' + '"' + " height='30' width='24' alt='Файл'/></td>"\
                "<td><a href='" + '{% static "' + request.GET['folder'] + elem[0] + '" %}' + "'" +\
                " download>" + "" + elem[
                0] + "</a></td>" \
                     "<td>" + date + "</td>" \
                     "<td>" + size + \
                     "&#160;</td><td><div id='edit'><a href='" + SITE_DELETE_FILE + "?delete=" + \
                current_file.replace(' ', '%20') + "' style='color: #2a5c03'>" + \
                "<img src='{% static 'images/trash_bin.png' %}' alt='Удалить файл' title='Удалить файл' height=30 width=26></a>" \
                "<a href='" + SITE_RENAME + "?current_name=" + rename_path + "' style='color: #2a5c03'> " \
                "<img src='{% static 'images/rename_icon.png' %}'" \
                " alt='Переименовать' title='Переименовать' width=30 height=30></a>" \
                "</div></td></tr>\n"
        current.pop(0)
    file = open(SERVER_PATH + "/files/templates/site.html", "w")
    ans += "</table></div></body>"
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