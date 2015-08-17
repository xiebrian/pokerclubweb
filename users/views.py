from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, loader
from .models import Member, Sponsor, Admin
from django.contrib.auth.models import User, Group
from pokerclubweb.forms import SponsorSignupForm, UserSignupForm
from .forms import MemberProfileForm, UserProfileForm, SponsorProfileForm, SponsorProfileAdminForm, AdminCreateForm, MemberSelectForm
from .decorators import group_required, is_self_or_admin
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request)
    context['members'] = Member.objects.all()
    return HttpResponse(template.render(context))

@login_required
def profile(request, userID=None):
    template = loader.get_template('users/profile.html')
    context = RequestContext(request)
    try:
        user = User.objects.get(id=userID)
        if hasattr(user, 'sponsor'):
            return redirect('sponsor_profile', user.id)
        elif hasattr(user, 'admin'):
            context['member'] = user.admin
        else:
            context['member'] = user.member
    except:
        return redirect('index')
    
    return HttpResponse(template.render(context))

@is_self_or_admin
def sponsor_profile(request, userID):
    template = loader.get_template('users/sponsors/profile.html')
    context = RequestContext(request)
    try:
        context['sponsor'] = Sponsor.objects.get(user=User.objects.get(id=userID))
    except:
        return redirect('index')
    
    return HttpResponse(template.render(context))

@is_self_or_admin
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
            member = sponsorform.save()

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

@group_required('member_group')
def edit_profile(request):
    if request.method == 'POST':
        userform = UserProfileForm(request.POST, prefix='user', instance=User.objects.get(id=request.user.id))
        memberform = MemberProfileForm(request.POST, request.FILES, prefix='member', instance=Member.objects.get(user=request.user))

        if (userform.is_valid() and memberform.is_valid()):
            user = userform.save()
            member = memberform.save()

            return redirect('profile', userID=user.id)
    else:
        userform = UserProfileForm(prefix='user', instance=User.objects.get(id=request.user.id))
        memberform = MemberProfileForm(prefix='member', instance=Member.objects.get(user=request.user))

    context = RequestContext(request)
    context['forms'] = [userform, memberform]
    if (userform.errors or memberform.errors):
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

@group_required('admin_group')
def admin_create_admin(request):
    if request.method == 'POST':
        memberform = MemberSelectForm(request.POST, prefix='member')
        adminform = AdminCreateForm(request.POST, prefix='admin')

        if (memberform.is_valid() and adminform.is_valid()):
            admin = adminform.save(commit=False)
            member = memberform.cleaned_data['member']
            Member.objects.filter(id=member.id).delete()
            admin.update_with_member(member)
            admin.save()
            
            g = Group.objects.get(name='admin_group')
            g.user_set.add(admin.user)

            g = Group.objects.get(name='member_group')
            g.user_set.remove(admin.user)

            return redirect('profile', userID=admin.user.id)
    else:
        memberform = MemberSelectForm(prefix='member')
        adminform = AdminCreateForm(prefix='admin')

    template = loader.get_template('users/admin/create.html')
    context = RequestContext(request)
    context['forms'] = [memberform, adminform]
    if (memberform.errors or adminform.errors):
        context['errors'] = True
    return HttpResponse(template.render(context))
