from django import forms
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'content', 'author']

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length = 50, help_text = 'Required Enter a valid Email')
#
#     class Meta:
#         model = User
#         fields = ['user', 'email', 'password1', 'password2',]

class SignUPForm(UserCreationForm):
    email = forms.EmailField(max_length = 50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
