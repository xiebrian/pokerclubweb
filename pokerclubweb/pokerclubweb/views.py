from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from users.models import Student, Sponsor
from django.contrib.auth.models import User, Group
from .forms import StudentSignupForm, UserSignupForm
from django.contrib.auth import forms as authforms
from django.contrib.auth import login as authLogin
from django.contrib.auth import logout as authLogout
from django.contrib.auth.views import password_reset, password_reset_confirm, password_change
from django.contrib.auth.decorators import login_required
from users.decorators import anonymous_required

@anonymous_required
def login(request):
    if request.method == 'POST':
        form = authforms.AuthenticationForm(data=request.POST)

        if (form.is_valid()):
            authLogin(request, form.get_user())
            return redirect('profile', userID=form.get_user().id)
    else:
        form = authforms.AuthenticationForm()

    template = loader.get_template('auth/login.html')
    context = RequestContext(request)
    context['forms'] = [form]
    if (form.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))

@anonymous_required
def signup(request):
    if request.method == 'POST':
        userform = UserSignupForm(request.POST, prefix='user')
        studentform = StudentSignupForm(request.POST, prefix='student')

        if (userform.is_valid() and studentform.is_valid()):
            user = userform.save()
            student = studentform.save(commit=False)
            student.user = user
            student.save()

            g = Group.objects.get(name='student_group')
            g.user_set.add(user)

            return redirect('index')
    else:
        userform = UserSignupForm(prefix='user')
        studentform = StudentSignupForm(prefix='student')

    template = loader.get_template('auth/signup.html')
    context = RequestContext(request)
    context['forms'] = [userform, studentform]
    if (userform.errors or studentform.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))

@login_required
def logout(request):
    authLogout(request)
    return redirect('index')

@login_required
def change_password(request):
    template_response = password_change(request, template_name='auth/change_password.html')
    if isinstance(template_response, TemplateResponse): 
        template_response.context_data['forms'] = [template_response.context_data['form']]
        if (template_response.context_data['form'].errors):
            template_response.context_data['errors'] = True
    return template_response

@login_required
def change_password_done(request):
    template = loader.get_template('auth/change_password_done.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

@anonymous_required
def reset_password(request):
    template_response = password_reset(request, email_template_name='auth/reset_password_email.html',  template_name='auth/reset_password.html')
    if isinstance(template_response, TemplateResponse): 
        template_response.context_data['forms'] = [template_response.context_data['form']]
        if (template_response.context_data['form'].errors):
            template_response.context_data['errors'] = True
    return template_response

@anonymous_required
def reset_password_done(request):
    template = loader.get_template('auth/reset_password_done.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

@anonymous_required
def reset_password_confirm(request, uidb64, token):
    template_response = password_reset_confirm(request, uidb64=uidb64, token=token, template_name='auth/reset_password_confirm.html')
    if isinstance(template_response, TemplateResponse): 
        template_response.context_data['forms'] = [template_response.context_data['form']]
        if (template_response.context_data['form'].errors):
            template_response.context_data['errors'] = True
    return template_response

@anonymous_required
def reset_password_complete(request):
    template = loader.get_template('auth/reset_password_complete.html')
    context = RequestContext(request)
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
    context['sponsors'] = Sponsor.objects.all()
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