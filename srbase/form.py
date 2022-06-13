from dataclasses import field
from msilib.schema import Class
from pyexpat import model
from django.forms import ModelForm
from .models import College,  Repository

class RepositoryForm(ModelForm):
    class Meta:
        model=Repository
        fields = '__all__'
        exclude = ['author', 'authors']
