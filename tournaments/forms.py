from django import forms
from .models import Tournament, TournamentResult
from users.forms import MemberModelChoiceField

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
        excludes = ['registered_members', 'results_available']
        help_texts = {
            'places' : ('Example: 3 means 1st, 2nd, and 3rd place will be tracked in the results')
        }

class TournamentResultForm(forms.ModelForm):

    class Meta:
        model = TournamentResult
        fields = ['member']

    def __init__(self, *args, **kwargs):
        place = kwargs.pop('place')
        tournament = kwargs.pop('tournament')
        super(TournamentResultForm, self).__init__(*args, **kwargs)

        self.fields['member'] = MemberModelChoiceField(tournament.registered_members, required=False, label=TournamentResult.intToWord(place) + " Place")