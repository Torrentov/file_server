from django import forms

class NewFolderForm(forms.Form):
    folder = forms.CharField(label='', label_suffix='',
                             widget=forms.TextInput(attrs={'style':
                                        'height:30px; font-size:20px; width:300px'
                                        'font-family:"Calibri"; margin-top:10px'}),
                             max_length=128)