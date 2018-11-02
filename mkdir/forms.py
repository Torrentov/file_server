from django.forms import ModelForm
from .models import Text

class NewFolderForm(ModelForm):
    class Meta:
        model = Text
        fields = ['folder']