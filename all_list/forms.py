from django import forms

class ToDoForm(forms.Form):
    end = forms.BooleanField()
    task = forms.CharField(max_length=100)
    limit = forms.DateField()
    memo = forms.CharField(max_length=500)