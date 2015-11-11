from django import forms
from django.contrib.auth.models import User
from users.models import Member, Sponsor, Admin
from django.forms import ModelChoiceField
from django.forms.models import BaseModelFormSet

class MemberModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return '{0} {1} ({2})'.format(obj.user.first_name, obj.user.last_name, obj.user)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {
            'username' : None
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

class MemberProfileForm(forms.ModelForm):
    is_interested_in_exec = forms.BooleanField(label='I am interesed in being contacted about joining the MIT Poker Club Committee', required=False)
    dropdowns = [
        'class_year'
    ]
    image_uploads = [
        'picture'
    ]
    file_uploads = image_uploads + [
        'resume'
    ]
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user', 'activation_key', 'is_registered']


class AdminProfileForm(MemberProfileForm):
    is_interested_in_exec = None
    dropdowns = [
        'class_year'
    ]
    image_uploads = [
        'picture'
    ]
    file_uploads = image_uploads + [
        'resume'
    ]
    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['user', 'activation_key', 'is_registered', 'officers_page_order', 'position']

class SponsorProfileForm(forms.ModelForm):

    class Meta:
        model = Sponsor
        fields = '__all__'
        exclude = ['user', 'level', 'logo', 'company_name', 'home_page_url']

class SponsorProfileAdminForm(forms.ModelForm):
    dropdowns = [
        'level'
    ]
    image_uploads = [
        'logo'
    ]
    file_uploads = image_uploads
    class Meta:
        model = Sponsor
        fields = '__all__'
        exclude = ['user']

class AdminCreateForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['position']

class MemberSelectForm(forms.Form):
    dropdowns = [
        'member'
    ]
    member = MemberModelChoiceField(Member.objects.all())

class AdminOfficersPageForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['position', 'officers_page_order']