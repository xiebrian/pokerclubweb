from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Student, Sponsor
from django.contrib.auth.models import User
from pokerclubweb.forms import SponsorSignupForm, UserSignupForm

def profile(request, userID=None):
    template = loader.get_template('users/profile.html')
    context = RequestContext(request)
    try:
        if not userID:
            print request.user.id
            context['student'] = Student.objects.get(user=request.user)
        else:
            print User.objects.get(id=userID)
            context['student'] = Student.objects.get(user=User.objects.get(id=userID))
    finally:
        return HttpResponse(template.render(context))

def edit_profile(request):
    template = loader.get_template('users/edit_profile.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def admin_tools(request):
    template = loader.get_template('users/admin/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

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
