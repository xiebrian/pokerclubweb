from django import forms
from django.contrib.auth.models import User
from users.models import Member, Sponsor, Admin
from django.forms import ModelChoiceField

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

class MemberProfileForm(forms.ModelForm):
    dropdowns = [
        'class_year'
    ]
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user', 'is_registered']
        

class AdminProfileForm(MemberProfileForm):
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
        exclude = ['user', 'is_registered']

class SponsorProfileForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'
        exclude = ['user', 'level']

class SponsorProfileAdminForm(forms.ModelForm):
    dropdowns = [
        'level'
    ]
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
