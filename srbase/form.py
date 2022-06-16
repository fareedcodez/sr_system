from dataclasses import field
from msilib.schema import Class
from pyexpat import model
from django.forms import ModelForm
from .models import College,  Repository
from django.contrib.auth.models import User

class RepositoryForm(ModelForm):
    class Meta:
        model=Repository
        fields = '__all__'
        exclude = ['author', 'authors', 'docfile']

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username', 'email']