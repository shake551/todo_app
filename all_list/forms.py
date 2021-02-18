from django import forms

class ToDoForm(forms.Form):
    end = forms.BooleanField(label='完了', required=False)
    task = forms.CharField(label='title', max_length=100)
    limit = forms.DateField(label='期限')
    memo = forms.CharField(label='詳細', max_length=500, required=False)