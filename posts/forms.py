from django import forms
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'creator', 'created_at', 'header_image')
        # widgets = {
        #     'body'
        #          
        # }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



# class PostForm(forms.Form):
#     body = forms.CharField(widget=forms.Textarea)
    