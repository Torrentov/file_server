from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.db import models
from .forms import UploadFileForm
from .models import Document
from server.vars import PATH, TMP_PATH, SITE
import os
from shutil import copyfile

# Create your views here.

def index(request):
    if not request.user.is_authenticated or request.session['auth'] != 1:
        return HttpResponseRedirect('/')
    needed_path = PATH + 'static/' + request.GET['folder']
    os.chdir(TMP_PATH)
    current_site = SITE + request.GET['folder']
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        current = str(form.cleaned_data['docfile'])
        files = os.listdir(path=needed_path)
        current_file = TMP_PATH + current
        i = 1
        while current in files:
            if current.count('(%s)' % str(i)) > 0:
                current = current.replace('(%s)' % str(i), '(%s)' % str(i + 1))
                i += 1
            else:
                current = current.split('.')
                current[0] += '(%s)' % str(i)
                current = current[0] + '.' + current[1]
        needed_path += current
        os.rename(current_file, PATH + needed_path.replace(PATH, ''))
        return HttpResponseRedirect(current_site.replace(' ', '%20'))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
