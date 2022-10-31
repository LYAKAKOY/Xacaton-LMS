from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'id': "login", 'type': "login", 'class': "input__field",
                                                             'name': "auth_login", 'placeholder': "login"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'type': "password", 'class': "input__field",
                                                                  'name': "auth_pass1", 'placeholder': "GoodPassword"}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'type': "password", 'class': "input__field",
                                                                  'name': "auth_pass2", 'placeholder': "GoodPassword"}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'type': "e-mail", 'class': "input__field",
                                                            'name': "auth_mail", 'placeholder': "ivan.ivanov@gmail.com"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
