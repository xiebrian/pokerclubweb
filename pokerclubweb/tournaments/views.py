from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from .forms import TournamentCreationForm, TournamentResultForm
from .models import Tournament, TournamentResult

def index(request):
    template = loader.get_template('tournaments/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def results(request):
    template = loader.get_template('tournaments/results.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def register(request):
    template = loader.get_template('tournaments/register.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def admin_create(request):
    if request.method == 'POST':
        form = TournamentCreationForm(data=request.POST)

        if (form.is_valid()):
            tournament = form.save()

        return redirect('admin_tools')
    else:
        form = TournamentCreationForm()

    template = loader.get_template('tournaments/admin/create.html')
    context = RequestContext(request)
    context['forms'] = [form]
    if (form.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))

def admin_results(request, tournamentID):
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
            forms.append(TournamentResultForm(prefix=n, place=n, tournament=tournament, instance=TournamentResult.objects.get(tournament=tournament, place=n)))

    template = loader.get_template('tournaments/admin/results.html')
    context = RequestContext(request)
    context['tournamentID'] = tournamentID
    context['forms'] = forms
    if any(form.errors for form in forms):
        context['errors'] = True
    return HttpResponse(template.render(context))

