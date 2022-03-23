from django import forms
from .models import content

class content_form(forms.ModelForm):
    class Meta:
        model =  content
        fields = ['username','email','body',]
class registerForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget= forms.PasswordInput)