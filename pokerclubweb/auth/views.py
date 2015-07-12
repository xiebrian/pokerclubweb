from django.http import HttpResponse
from django.template import RequestContext, loader

def login(request):
    template = loader.get_template('auth/login.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def signup(request):
    template = loader.get_template('auth/signup.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))