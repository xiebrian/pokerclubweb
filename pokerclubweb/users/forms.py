from django import forms
from django.contrib.auth.models import User
from users.models import Student, Sponsor


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {
            'username' : None
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user', 'is_member']

class SponsorProfileForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'
        exclude = ['user', 'level']

class SponsorProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'
        exclude = ['user']
