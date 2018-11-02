from django.forms import ModelForm
from .models import Document

class UploadFileForm(ModelForm):
    class Meta:
        model = Document
        fields = ['docfile']