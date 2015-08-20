from django import forms
from django.utils import six
from .models import Tournament, TournamentResult
from users.forms import MemberModelChoiceField
from users.models import Member

class SemanticModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def clean(self, value):
        print value
        cleaned_value = []
        for item in value:
            cleaned_value.extend(item.split(','))
        print cleaned_value
        return super(SemanticModelMultipleChoiceField, self).clean(cleaned_value)

    def prepare_value(self, value):
        print value
        if (hasattr(value, '__iter__') and
                not isinstance(value, six.text_type) and
                not hasattr(value, '_meta')):
            return ",".join([str(super(SemanticModelMultipleChoiceField, self).prepare_value(v)) for v in value])
        return super(SemanticModelMultipleChoiceField, self).prepare_value(value)

class TournamentCreationForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(attrs={'type':'datetime-local'}),
    )
    end_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(attrs={'type':'datetime-local'})
    )
    class Meta:
        model = Tournament
        fields = '__all__'
        exclude = ['registered_members', 'results_available', 'registration_open']
        help_texts = {
            'places' : ('Example: 3 means 1st, 2nd, and 3rd place will be tracked in the results')
        }

class TournamentEditForm(TournamentCreationForm):
    multiple_selects = [
        'registered_members'
    ]
    checkboxes = [
        'results_available',
        'registration_open'
    ]
    dropdowns = multiple_selects
    registered_members = SemanticModelMultipleChoiceField(queryset=Member.objects.all())
    class Meta:
        model = Tournament
        fields = '__all__'
        #exclude = ['registered_members']
        help_texts = {
            'places' : ('Example: 3 means 1st, 2nd, and 3rd place will be tracked in the results')
        }

    # def clean(self):
    #     data = self.cleaned_data['registered_members']
    #     print data
    #     return data

class TournamentResultForm(forms.ModelForm):

    class Meta:
        model = TournamentResult
        fields = ['member']

    def __init__(self, *args, **kwargs):
        place = kwargs.pop('place')
        tournament = kwargs.pop('tournament')
        super(TournamentResultForm, self).__init__(*args, **kwargs)

        self.fields['member'] = MemberModelChoiceField(tournament.registered_members, required=False, label=TournamentResult.intToWord(place) + " Place")