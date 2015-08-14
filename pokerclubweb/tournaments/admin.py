from django.contrib import admin

from .models import Tournament, TournamentResult

admin.site.register(Tournament)
admin.site.register(TournamentResult)