from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('home/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('home/about.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def events(request):
    template = loader.get_template('home/events.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def sponsors(request):
    template = loader.get_template('home/sponsors.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def officers(request):
    template = loader.get_template('home/officers.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def photos(request):
    template = loader.get_template('home/photos.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('home/contact.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))