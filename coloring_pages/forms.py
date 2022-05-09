
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User=get_user_model()

class Register(UserCreationForm):
    password1 = forms.CharField(label='Пароль', required=False,
                                widget=forms.PasswordInput(attrs={"cols": 40, "rows": 6, 'id': 'textArea'}))
    password2 = forms.CharField(label='Повтор пароля', required=False,
                                widget=forms.PasswordInput(attrs={"cols": 40, "rows": 6, 'id': 'textArea'}))
    class Meta:
        model=User
        fields = ("username", 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'id': 'textArea'}),
            'password1': forms.PasswordInput(attrs={'id': 'textArea'}),
            'password2': forms.PasswordInput(attrs={'id': 'textArea'})
        }
