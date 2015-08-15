from django import forms
from .models import Tournament, TournamentResult

class TournamentCreationForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'start_time', 'end_time', 'location']
        widgets = {
            'start_time' : forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'end_time' : forms.DateTimeInput(attrs={'type':'datetime-local'})
        }