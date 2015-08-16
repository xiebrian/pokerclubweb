from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from .forms import TournamentCreationForm, TournamentResultForm
from .models import Tournament, TournamentResult

def index(request):
    template = loader.get_template('tournaments/index.html')
    context = RequestContext(request)
    context['tournaments'] = Tournament.objects.all()
    return HttpResponse(template.render(context))

def summary(request, tournamentID):
    template = loader.get_template('tournaments/summary.html')
    context = RequestContext(request)
    context['tournament'] = Tournament.objects.get(id=tournamentID)
    try:
        context['isRegistered'] = request.user.student in context['tournament'].registered_students.all()
    except:
        context['isRegistered'] = False
    return HttpResponse(template.render(context))

def results(request, tournamentID):
    template = loader.get_template('tournaments/results.html')
    context = RequestContext(request)
    context['tournament'] = Tournament.objects.get(id=tournamentID)
    return HttpResponse(template.render(context))

def register(request, tournamentID):
    if request.method == 'POST':
        tournament = Tournament.objects.get(id=tournamentID)
        student = request.user.student

        if student in tournament.registered_students.all():
            tournament.registered_students.remove(student)
        else:
            tournament.registered_students.add(student)

        tournament.save()

    return redirect('summary', tournamentID=tournamentID)

def admin_create_tournament(request, tournamentID=0):

    if request.method == 'POST':
        if (tournamentID):
            tournament = Tournament.objects.get(id=tournamentID)
            form = TournamentCreationForm(data=request.POST, instance=tournament)
        else:
            form = TournamentCreationForm(data=request.POST)

        if (form.is_valid()):
            tournament = form.save()
            tournamentID = tournament.id

            return redirect('summary', tournamentID=tournamentID)
    else:
        if (tournamentID):
            tournament = Tournament.objects.get(id=tournamentID)
            print tournament.start_time.strftime('%Y-%m-%dT%H:%M')
            print tournament.start_time
            form = TournamentCreationForm(
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
    return HttpResponse(template.render(context))

def admin_edit_tournament_results(request, tournamentID):
    tournament = Tournament.objects.get(id=tournamentID)
    forms = []
    if request.method == 'POST':
        for n in range(1,tournament.places+1):
            forms.append(TournamentResultForm(data=request.POST, prefix=n, place=n, tournament=tournament))

        if all(form.is_valid() for form in forms):
            for form in forms:
                result = form.save(commit=False)
                result.tournament = tournament
                result.place = form.prefix
                result.save()

            return redirect('admin_tools')
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
    return HttpResponse(template.render(context))

