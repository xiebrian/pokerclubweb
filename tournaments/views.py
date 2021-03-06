from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from .forms import TournamentCreationForm, TournamentEditForm, TournamentResultForm
from .models import Tournament, TournamentResult
from django.db import IntegrityError
from django.forms.util import ErrorList
from users.decorators import group_required

def index(request):
    template = loader.get_template('tournaments/index.html')
    context = RequestContext(request)
    context['tournaments'] = Tournament.objects.all()
    context['title'] = 'Tournaments'
    return HttpResponse(template.render(context))

def summary(request, tournamentID):
    template = loader.get_template('tournaments/summary.html')
    context = RequestContext(request)
    tournament = Tournament.objects.get(id=tournamentID)
    context['tournament'] = Tournament.objects.get(id=tournamentID)
    try:
        context['isRegistered'] = request.user.member in tournament.registered_members.all()
    except:
        context['isRegistered'] = False

    if tournament.results_available:
        context['results'] = TournamentResult.objects.filter(tournament=tournament)

    context['title'] = tournament.name
    return HttpResponse(template.render(context))

@group_required('member_group')
def register(request, tournamentID):
    if request.method == 'POST':
        tournament = Tournament.objects.get(id=tournamentID)
        member = request.user.member

        if member in tournament.registered_members.all():
            tournament.registered_members.remove(member)
        else:
            tournament.registered_members.add(member)

        tournament.save()

    return redirect('summary', tournamentID=tournamentID)

@group_required('admin_group')
def admin_create_tournament(request, tournamentID=0):

    if request.method == 'POST':
        # print request.POST
        if (tournamentID):
            tournament = Tournament.objects.get(id=tournamentID)
            form = TournamentEditForm(data=request.POST, instance=tournament)
        else:
            form = TournamentCreationForm(data=request.POST)

        if (form.is_valid()):
            tournament = form.save()
            tournamentID = tournament.id

            return redirect('summary', tournamentID=tournamentID)
    else:
        if (tournamentID):
            tournament = Tournament.objects.get(id=tournamentID)
            #print tournament.start_time.strftime('%Y-%m-%dT%H:%M')
            #print tournament.start_time
            form = TournamentEditForm(
                instance=tournament,
                initial = {
                    'start_time' : tournament.start_time.strftime('%Y-%m-%dT%H:%M'),
                    'end_time' : tournament.end_time.strftime('%Y-%m-%dT%H:%M'),
            })
        else:
            form = TournamentCreationForm()

    template = loader.get_template('tournaments/admin/create.html')
    context = RequestContext(request)
    context['forms'] = [form]
    if (form.errors):
        context['errors'] = True
    context['title'] = 'Create Tournament'
    return HttpResponse(template.render(context))

@group_required('admin_group')
def admin_edit_tournament_results(request, tournamentID):
    tournament = Tournament.objects.get(id=tournamentID)
    forms = []
    if request.method == 'POST':
        for n in range(1,tournament.places+1):
            instance, _ = TournamentResult.objects.get_or_create(tournament=tournament, place=n)
            forms.append(TournamentResultForm(data=request.POST, prefix=n, place=n, tournament=tournament, instance=instance))

        if all(form.is_valid() for form in forms):
            members = {}
            for form in forms:
                result = form.save(commit=False)
                members[form]=result.member
                result.member = None
                result.save()
            error = False
            for form in forms:
                result = form.save(commit=False)
                result.member = members[form]
                try:
                    result.save()
                except IntegrityError:
                    errors = form._errors.setdefault('member', ErrorList())
                    errors.append(u'This member was selected for multiple places')
                    error = True

            if not error:
                return redirect('summary', tournamentID=tournamentID)
    else:
        for n in range(1,tournament.places+1):
            instance, _ = TournamentResult.objects.get_or_create(tournament=tournament, place=n)
            forms.append(TournamentResultForm(prefix=n, place=n, tournament=tournament, instance=instance))

    template = loader.get_template('tournaments/admin/results.html')
    context = RequestContext(request)
    context['tournamentID'] = tournamentID
    context['forms'] = forms
    if any(form.errors for form in forms):
        context['errors'] = True
    context['title'] = 'Edit Results for ' + tournament.name
    return HttpResponse(template.render(context))

