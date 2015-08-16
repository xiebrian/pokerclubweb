from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from .models import Student, Sponsor
from django.contrib.auth.models import User, Group
from pokerclubweb.forms import SponsorSignupForm, UserSignupForm
from .forms import StudentProfileForm, UserProfileForm, SponsorProfileForm, SponsorProfileAdminForm
from .decorators import group_required, is_self_or_admin

def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request)
    context['students'] = Student.objects.all()
    return HttpResponse(template.render(context))

def profile(request, userID=None):
    template = loader.get_template('users/profile.html')
    context = RequestContext(request)
    try:
        if not userID:
            context['student'] = Student.objects.get(user=request.user)
        else:
            context['student'] = Student.objects.get(user=User.objects.get(id=userID))
    finally:
        return HttpResponse(template.render(context))

@is_self_or_admin
def sponsor_profile(request, userID):
    template = loader.get_template('users/sponsors/profile.html')
    context = RequestContext(request)
    try:
        context['sponsor'] = Sponsor.objects.get(user=User.objects.get(id=userID))
    except:
        return redirect('sponsors')
    
    return HttpResponse(template.render(context))


def edit_sponsor_profile(request, userID):
    user = User.objects.get(id=userID)
    SponsorFormClass = SponsorProfileForm
    if request.user.groups.filter(name="admin_group").exists():
        SponsorFormClass = SponsorProfileAdminForm
    if request.method == 'POST':
        userform = UserProfileForm(request.POST, prefix='user', instance=user)
        sponsorform = SponsorFormClass(request.POST, request.FILES, prefix='sponsor', instance=Sponsor.objects.get(user=user))

        if (userform.is_valid() and sponsorform.is_valid()):
            user = userform.save()
            student = sponsorform.save()

            return redirect('sponsor_profile', userID=user.id)
    else:
        userform = UserProfileForm(prefix='user', instance=user)
        sponsorform = SponsorFormClass(prefix='sponsor', instance=Sponsor.objects.get(user=user))

    context = RequestContext(request)
    context['forms'] = [userform, sponsorform]
    if (userform.errors or sponsorform.errors):
        context['errors'] = True
    template = loader.get_template('users/sponsors/edit_profile.html')
    return HttpResponse(template.render(context))

@group_required('student_group')
def edit_profile(request):
    if request.method == 'POST':
        userform = UserProfileForm(request.POST, prefix='user', instance=User.objects.get(id=request.user.id))
        studentform = StudentProfileForm(request.POST, request.FILES, prefix='student', instance=Student.objects.get(user=request.user))

        if (userform.is_valid() and studentform.is_valid()):
            user = userform.save()
            student = studentform.save()

            return redirect('profile', userID=user.id)
    else:
        userform = UserProfileForm(prefix='user', instance=User.objects.get(id=request.user.id))
        studentform = StudentProfileForm(prefix='student', instance=Student.objects.get(user=request.user))

    context = RequestContext(request)
    context['forms'] = [userform, studentform]
    if (userform.errors or studentform.errors):
        context['errors'] = True
    template = loader.get_template('users/edit_profile.html')
    return HttpResponse(template.render(context))

@group_required('admin_group')
def admin_tools(request):
    template = loader.get_template('users/admin/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

@group_required('admin_group')
def admin_create_sponsor(request, sponsorID=0):
    if request.method == 'POST':
        if (sponsorID):
            sponsor = Sponsor.objects.get(id=SponsorID)
            user = sponsor.user
            userform = UserSignupForm(request.POST, prefix='user', instance=user)
            sponsorform = SponsorSignupForm(request.POST, prefix='sponsor', instance=sponsor)
        else:
            userform = UserSignupForm(request.POST, prefix='user')
            sponsorform = SponsorSignupForm(request.POST, prefix='sponsor')

        if (userform.is_valid() and sponsorform.is_valid()):
            user = userform.save()
            sponsor = sponsorform.save(commit=False)
            sponsor.user = user
            sponsor.save()

            g = Group.objects.get(name='sponsor_group')
            g.user_set.add(user)

            return redirect('profile', userID=user.id)
    else:
        if (sponsorID):
            sponsor = Sponsor.objects.get(id=SponsorID)
            user = sponsor.user
            userform = UserSignupForm(prefix='user', instance=user)
            sponsorform = SponsorSignupForm(prefix='sponsor', instance=sponsor)
        else:
            userform = UserSignupForm(prefix='user')
            sponsorform = SponsorSignupForm(prefix='sponsor')

    template = loader.get_template('users/admin/sponsors/create.html')
    context = RequestContext(request)
    context['forms'] = [userform, sponsorform]
    if (userform.errors or sponsorform.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))
