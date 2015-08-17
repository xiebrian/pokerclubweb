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
    class Meta:
        model = Member
        fields = ['class_year']

class SponsorSignupForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['company_name', 'level']