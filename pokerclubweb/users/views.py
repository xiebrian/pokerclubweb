from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Student
from django.contrib.auth.models import User

def profile(request, userID=None):
    template = loader.get_template('users/profile.html')
    context = RequestContext(request)
    if not userID:
        print request.user.id
        context['student'] = Student.objects.get(user=request.user)
    else:
        print User.objects.get(id=userID)
        context['student'] = Student.objects.get(user=User.objects.get(id=userID))

    return HttpResponse(template.render(context))

def edit_profile(request):
    template = loader.get_template('users/edit_profile.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def admin_tools(request):
    template = loader.get_template('users/admin/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))