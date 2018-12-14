from django.forms import ModelForm, FileField
from .models import Document
from django.utils.translation import ugettext_lazy as _

class UploadFileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['docfile'].widget.attrs.update({'style': 'height:30px;'
                                                             'font-size:20px;'
                                                             'font-family:"Calibri";'})
    class Meta:
        model = Document
        fields = ['docfile']
        labels = {
            'docfile': _('Выберите файл для загрузки: '),
        }
