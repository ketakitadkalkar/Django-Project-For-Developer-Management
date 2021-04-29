from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from django.db import models

from .models import Developer, Employee

from .models import Technology


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('username', 'password')


form = LoginForm()


class EditForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'email', 'location', 'experience', 'technology', 'domain', 'blogs','blog_weightage', 'project','project_weightage', 'question','QA_weightage',
                  'score']

    # Name = models.CharField(max_length = 200)
form=EditForm()


class Edit(forms.ModelForm):
    class Meta:
        model=Developer
        fields= ['name']
form = Edit()

class AddDeveloper(ModelForm):
    class Meta:
        model = Developer

        fields = ['name', 'email', 'location', 'experience', 'technology', 'domain', 'blogs','blog_weightage', 'project', 'project_weightage' ,'question',
                 'QA_weightage', 'score']

    # Creating a form to add an article.


form = AddDeveloper()

class Search(ModelForm):
    class Meta:
        model = Developer
        fields = ['location', 'technology', 'domain']

form= Search()
