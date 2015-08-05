from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from users.models import Student
from django.contrib.auth.models import User
from .forms import StudentSignupForm, UserSignupForm
from django.forms.models import inlineformset_factory

def login(request):
    template = loader.get_template('auth/login.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def signup(request):
    #signup_form = inlineformset_factory(Student, User, fields=('username','password1','password2','classyear',))
    # if request.method == 'POST':
    #     form = StudentSignupForm(request.POST)

    #     if (form.is_valid()):
    #         user = User.objects.create_user(form)
    #         student = Student.objects.create(user=user)
    #         user.save()
    #         student.save()

    #         return HttpResponseRedirect('/')
    # else:
    #     form = StudentSignupForm()

    # template = loader.get_template('auth/signup.html')
    # context = RequestContext(request)
    # context['form'] = form
    # return HttpResponse(template.render(context))
    if request.method == 'POST':
        userform = UserSignupForm(request.POST, prefix='user')
        studentform = StudentSignupForm(request.POST, prefix='student')

        if (userform.is_valid() and studentform.is_valid()):
            user = User.objects.create_user(userform)
            student = Student.objects.create(studentform, user=user)
            user.save()
            student.save()

            return HttpResponseRedirect('/')
    else:
        userform = UserSignupForm(prefix='user')
        studentform = StudentSignupForm(prefix='student')

    template = loader.get_template('auth/signup.html')
    context = RequestContext(request)
    context['userform'] = userform
    context['studentform'] = studentform
    return HttpResponse(template.render(context))