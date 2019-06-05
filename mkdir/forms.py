from django import forms

class NewFolderForm(forms.Form):
    folder = forms.CharField(label='', label_suffix='',
                             widget=forms.TextInput(attrs={'style':
                                        'font-size: 100; width:100%;'
                                        'font-family:"Calibri"; margin-top:10px;'
                                        'verrical-align: middle;'}),
                             max_length=128)