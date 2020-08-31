from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    sex = forms.CharField(max_length=1)
    phone_number = forms.CharField(max_length=12)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'sex', 'phone_number', 'birth_date', 'password1', 'password2')

