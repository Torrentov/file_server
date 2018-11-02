from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from .forms import NewFolderForm
from server.vars import PATH, SITE

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        current_site = SITE + request.GET['folder'].replace(PATH, '')
        real_path = request.GET['folder']
        form = NewFolderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['folder']
            files = os.listdir(real_path)
            i = 1
            while name in files:
                if name.count('(%s)' % str(i)) > 0:
                    name = name.replace('(%s)' % str(i), '(%s)' % str(i + 1))
                    i += 1
                else:
                    name += '(%s)' % str(i)
            os.mkdir(real_path + name)
            os.mkdir(PATH + "static/" + real_path.replace(PATH, '') + name)
            return HttpResponseRedirect(current_site)
    else:
        form = NewFolderForm()
    return render(request, 'folder.html', {'form': form, 'folder': request.GET['folder']})
