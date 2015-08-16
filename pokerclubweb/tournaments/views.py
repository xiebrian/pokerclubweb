from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from .forms import TournamentCreationForm, TournamentResultForm
from .models import Tournament, TournamentResult
from django.db import IntegrityError
from django.forms.util import ErrorList
from users.decorators import group_required

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

    if context['tournament'].results_available:
        try:
            context['results'] = TournamentResult.objects.filter(tournament=context['tournament'])
        except:
            print 'ERROR'

    return HttpResponse(template.render(context))

@group_required('student_group')
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

@group_required('admin_group')
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

@group_required('admin_group')
def admin_edit_tournament_results(request, tournamentID):
    tournament = Tournament.objects.get(id=tournamentID)
    forms = []
    if request.method == 'POST':
        for n in range(1,tournament.places+1):
            instance, _ = TournamentResult.objects.get_or_create(tournament=tournament, place=n)
            forms.append(TournamentResultForm(data=request.POST, prefix=n, place=n, tournament=tournament, instance=instance))

        if all(form.is_valid() for form in forms):
            students = {}
            for form in forms:
                result = form.save(commit=False)
                students[form]=result.student
                result.student = None
                result.save()
            error = False
            for form in forms:
                result = form.save(commit=False)
                result.student = students[form]
                try:
                    result.save()
                except IntegrityError:
                    errors = form._errors.setdefault('student', ErrorList())
                    errors.append(u'This student was selected for multiple places')
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
    return HttpResponse(template.render(context))

