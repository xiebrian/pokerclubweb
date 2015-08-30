from django import forms
from django.contrib.auth import forms as authforms
from django.contrib.auth.models import User
from users.models import Member, Sponsor


class UserSignupForm(authforms.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

class MemberSignupForm(forms.ModelForm):
    dropdowns = [
        'class_year'
    ]
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user', 'is_registered']

class SponsorSignupForm(forms.ModelForm):
    dropdowns = [
        'level'
    ]
    class Meta:
        model = Sponsor
        fields = '__all__'
        exclude = ['user']