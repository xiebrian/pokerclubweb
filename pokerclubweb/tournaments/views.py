from django.http import HttpResponse
from django.template import RequestContext, loader

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