from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from users.models import Student
from django.contrib.auth.models import User, Group
from .forms import StudentSignupForm, UserSignupForm
from django.contrib.auth import forms as authforms
from django.contrib.auth import login as authLogin

def login(request):
    if request.method == 'POST':
        form = authforms.AuthenticationForm(data=request.POST)

        for error in form.errors:
            print error
        print form.errors
        if (form.is_valid()):
            authLogin(request, form.get_user())
            return HttpResponseRedirect('/users/profile')
    else:
        form = authforms.AuthenticationForm()

    template = loader.get_template('auth/login.html')
    context = RequestContext(request)
    context['forms'] = [form]
    if (form.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))

def signup(request):
    if request.method == 'POST':
        userform = UserSignupForm(request.POST, prefix='user')
        studentform = StudentSignupForm(request.POST, prefix='student')
        # print 'student valid: ' + str(studentform.is_valid())
        # print 'user valid: ' + str(userform.is_valid())

        if (userform.is_valid() and studentform.is_valid()):
            user = userform.save()
            student = studentform.save(commit=False)
            student.user = user
            student.save()

            g = Group.objects.get(name='student_group')
            g.user_set.add(user)

            return HttpResponseRedirect('/')
    else:
        userform = UserSignupForm(prefix='user')
        studentform = StudentSignupForm(prefix='student')

    template = loader.get_template('auth/signup.html')
    context = RequestContext(request)
    context['forms'] = [userform, studentform]
    if (userform.errors or studentform.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))

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