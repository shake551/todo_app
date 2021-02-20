from django import forms

class ToDoForm(forms.Form):
    end = forms.BooleanField(label='完了', required=False)
    task = forms.CharField(label='title', max_length=100)
    limit = forms.DateField(label='期限',
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d'])
    limit_time = forms.DateTimeField(label='時間',
        widget=forms.DateTimeInput(attrs={"type": "time"}),
        input_formats=['%H:%i'],
        required=False)
    memo = forms.CharField(label='詳細', max_length=500, required=False)