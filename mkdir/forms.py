from django.forms import ModelForm, Textarea
from .models import Text
from django.utils.translation import ugettext_lazy as _

class NewFolderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewFolderForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
    class Meta:
        model = Text
        labels = {
            'folder': _(''),
        }
        widgets = {
            'folder': Textarea(attrs={'style': 'height:30px; font-size:20px; '
                                        'font-family:"Calibri"; margin-top:10px'})
        }
        fields = ['folder']