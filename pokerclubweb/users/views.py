from django.http import HttpResponse
from django.template import RequestContext, loader

def profile(request):
    template = loader.get_template('users/profile.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def edit_profile(request):
    template = loader.get_template('users/edit_profile.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))