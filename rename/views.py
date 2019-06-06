from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from .forms import RenameForm
from server.vars import PATH, SITE, SERVER_PATH, FONT_PATH
from time import time

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        current_name = request.GET['current_name']
        current_site = SITE + current_name.replace(PATH + 'static/', '')
        real_path = request.GET['current_name'].split('/')
        real_path.pop()
        if current_name[-1] == '/':
            real_path.pop()
        a = ''
        for elem in real_path:
            a += elem + '/'
        real_path = a
        if current_name[-1] == '/':
            current_name = current_name.split('/')[:-1]
            a = ''
            for elem in current_name:
                a += elem + '/'
            current_name = a
        form = RenameForm(request.POST, label_suffix="huy")
        if form.is_valid():
            name = form.cleaned_data['name']
            files = os.listdir(real_path)
            i = 1
            while name in files:
                if name.count('(%s)' % str(i)) > 0:
                    name = name.replace('(%s)' % str(i), '(%s)' % str(i + 1))
                    i += 1
                else:
                    name += '(%s)' % str(i)
            os.rename(current_name, real_path + name)
            current_name = current_name.replace(PATH, '').split('/')[-1]
            return HttpResponseRedirect(current_site.replace(' ', '%20').replace(current_name, ''))
    else:
        form = RenameForm()
    return render(request, 'rename.html', {'form': form, 'current_name': request.GET['current_name'],
                                           'FONT': FONT_PATH})
