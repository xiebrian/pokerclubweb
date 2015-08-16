from django import forms
from .models import Tournament, TournamentResult
from users.models import Student
from django.forms import ModelChoiceField
from datetime import datetime

class StudentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return '{0} {1} ({2})'.format(obj.user.first_name, obj.user.last_name, obj.user)

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
        fields = ['name', 'start_time', 'end_time', 'location', 'places']
        help_texts = {
            'places' : ('Example: 3 means 1st, 2nd, and 3rd place will be tracked in the results')
        }

class TournamentResultForm(forms.ModelForm):

    class Meta:
        model = TournamentResult
        fields = ['student']

    def __init__(self, *args, **kwargs):
        place = kwargs.pop('place')
        tournament = kwargs.pop('tournament')
        super(TournamentResultForm, self).__init__(*args, **kwargs)

        self.fields['student'] = StudentModelChoiceField(tournament.registered_students, label=TournamentResult.intToWord(place) + " Place")