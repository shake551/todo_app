from django import forms
from django.forms import ModelForm

from .models import ToDo

class ToDoForm(forms.ModelForm):
    end = forms.BooleanField(label='完了', required=False)
    task = forms.CharField(label='title', max_length=100)
    limit = forms.DateField(label='期限',
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d'])
    memo = forms.CharField(label='詳細', max_length=500, required=False)
    
    class Meta:
        model = ToDo
        fields = ['end', 'task', 'limit', 'memo']