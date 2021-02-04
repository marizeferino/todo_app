from django import forms
from django.forms import fields
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Adicione aqui uma nova tarefa...'}))

    class Meta:
        model = Task
        fields = '__all__'