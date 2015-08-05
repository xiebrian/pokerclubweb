from django import forms
from django.contrib.auth import forms as authforms
from django.contrib.auth.models import User
from users.models import Student


class UserSignupForm(authforms.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['classyear']