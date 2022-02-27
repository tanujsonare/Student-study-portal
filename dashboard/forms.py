from  django import forms
from .models import *
# from django.forms.widgets import(HiddenInput)


class NotesForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Note
        fields = ['title', 'description','user']
       
      

    
    