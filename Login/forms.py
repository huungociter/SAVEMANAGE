from django import forms
from .models import content

class content_form(forms.ModelForm):
    class Meta:
        model =  content
        fields = ['username','email','body',]