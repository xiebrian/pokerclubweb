from django import forms
from django.contrib.auth import forms as authforms
from django.contrib.auth.models import User
from users.models import Member, Sponsor
from django.core.validators import RegexValidator

validate_mit_domain = RegexValidator(regex='^[A-Za-z0-9._%+-]+@mit.edu$', message='Please enter an @mit.edu email address')

class UserSignupForm(authforms.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    #clean email field
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already in use')

    #modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):        
        user = super(UserSignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()

        return user

class UserSignupMITEmailForm(UserSignupForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': None,
            'email': 'Enter an @mit.edu email address'
        }
   
    def __init__(self, *args, **kwargs):
        super(UserSignupMITEmailForm, self).__init__(*args, **kwargs)

        #require mit.edu domain
        self.fields['email'].validators = [validate_mit_domain]
        


class MemberSignupForm(forms.ModelForm):
    is_interested_in_exec = forms.BooleanField(label='I am interested in being contacted about joining the MIT Poker Club Committee', required=False)
    dropdowns = [
        'class_year'
    ]
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user', 'bio', 'activation_key', 'resume', 'picture', 'is_registered']

class SponsorSignupForm(forms.ModelForm):
    dropdowns = [
        'level'
    ]
    class Meta:
        model = Sponsor
        fields = '__all__'
        exclude = ['user']