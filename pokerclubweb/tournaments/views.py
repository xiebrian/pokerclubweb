from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms import TournamentCreationForm

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
    else:
        form = TournamentCreationForm()

    template = loader.get_template('tournaments/admin/create.html')
    context = RequestContext(request)
    context['forms'] = [form]
    if (form.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))

def admin_results(request, tournamentID):
    template = loader.get_template('tournaments/admin/results.html')
    context = RequestContext(request)
    context['tournamentID'] = tournamentID
    return HttpResponse(template.render(context))

