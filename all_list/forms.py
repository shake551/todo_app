from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

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

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, label='username')
    enter_password = forms.CharField(widget=forms.PasswordInput, label='enter_password')
    retype_password = forms.CharField(widget=forms.PasswordInput, label='retype_password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username has been already taken.')
        return username

    def clean_enter_password(self):
        password = self.cleaned_data.get('enter_password')
        if len(password) < 5:
            raise forms.ValidationError('Password must contain 5 or more characters.')
        return password

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('enter_password')
        retyped = self.cleaned_data.get('retype_password')
        if password and retyped and (password != retyped):
            self.add_error('retype_password', 'This does not match with the above.')

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('enter_password')
        new_user = User.objects.create_user(username = username)
        new_user.set_password(password)
        new_user.save()

    class Meta:
        fields = ['username', 'enter_password', 'retype_password']