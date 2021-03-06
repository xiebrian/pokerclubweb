from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.template import RequestContext, loader
from .models import Member, Sponsor, Admin, Student
from django.contrib.auth.models import User, Group
from pokerclubweb.forms import SponsorSignupForm, UserSignupForm
from .forms import *
from .decorators import group_required, is_self_or_admin, can_view_resumes
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory

import os
import csv

@login_required
def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request)
    context['members'] = sorted(Member.objects.all(), key=lambda member: member.user.first_name)
    context['title'] = 'Members'
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
    context['title'] = context['member'].full_name
    return HttpResponse(template.render(context))

@can_view_resumes
def view_resume(request, userID):
    user = User.objects.get(id=userID)
    if hasattr(user, 'member'):
        resume = user.member.resume
    elif hasattr(user, 'admin'):
        resume = user.admin.resume
    else:
        return redirect('index')

    try:
        if resume:
            abspath = open(str(resume.file),'r')
            response = HttpResponse(content=abspath.read())

            response['Content-Type'] = 'application/pdf'

            response['Content-Disposition'] = 'inline; filename=%s.pdf' \
                % (user.first_name+'_'+user.last_name)
            return response
        else:
            return redirect('profile', userID=userID)
    except IOError:
        return redirect('profile', userID=userID)

@is_self_or_admin
def sponsor_profile(request, userID):
    template = loader.get_template('users/sponsors/profile.html')
    context = RequestContext(request)
    try:
        context['sponsor'] = Sponsor.objects.get(user=User.objects.get(id=userID))
    except:
        return redirect('index')

    context['title'] = context['sponsor'].company_name
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
    context['title'] = 'Edit Profile for ' + user.sponsor.company_name
    return HttpResponse(template.render(context))

@group_required('member_group', 'admin_group')
def edit_profile(request):
    if request.method == 'POST':
        userform = UserProfileForm(request.POST, prefix='user', instance=User.objects.get(id=request.user.id))
        if hasattr(request.user, 'admin'):
            memberform = AdminProfileForm(request.POST, request.FILES, prefix='member', instance=Admin.objects.get(user=request.user))
        else:
            memberform = MemberProfileForm(request.POST, request.FILES, prefix='member', instance=Member.objects.get(user=request.user))

        if (userform.is_valid() and memberform.is_valid()):
            user = userform.save()
            member = memberform.save()

            return redirect('profile', userID=user.id)
    else:
        userform = UserProfileForm(prefix='user', instance=User.objects.get(id=request.user.id))
        if hasattr(request.user, 'admin'):
            memberform = AdminProfileForm(prefix='member', instance=Admin.objects.get(user=request.user))
        else:
            memberform = MemberProfileForm(prefix='member', instance=Member.objects.get(user=request.user))

    context = RequestContext(request)
    context['forms'] = [userform, memberform]
    if (userform.errors or memberform.errors):
        context['errors'] = True
    template = loader.get_template('users/edit_profile.html')
    context['title'] = 'Edit Profile'
    context['caption'] = '(If you see nothing, email: poker@mit.edu)'
    return HttpResponse(template.render(context))

@group_required('admin_group')
def admin_tools(request):
    template = loader.get_template('users/admin/index.html')
    context = RequestContext(request)
    context['title'] = 'Admin Tools'
    return HttpResponse(template.render(context))

@group_required('admin_group')
def admin_create_sponsor(request, sponsorID=0):
    if request.method == 'POST':
        if (sponsorID):
            sponsor = Sponsor.objects.get(id=SponsorID)
            user = sponsor.user
            userform = UserSignupForm(request.POST, prefix='user', instance=user)
            sponsorform = SponsorSignupForm(request.POST, request.FILES, prefix='sponsor', instance=sponsor)
        else:
            userform = UserSignupForm(request.POST, prefix='user')
            sponsorform = SponsorSignupForm(request.POST, request.FILES, prefix='sponsor')

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
    context['title'] = 'Create Sponsor'
    return HttpResponse(template.render(context))

@group_required('admin_group')
def admin_create_admin(request):
    if request.method == 'POST':
        memberform = MemberSelectForm(request.POST, prefix='member')
        adminform = AdminCreateForm(request.POST, prefix='admin')

        if (memberform.is_valid() and adminform.is_valid()):
            admin = adminform.save(commit=False)
            member = memberform.cleaned_data['member']
            admin.update_with_member(member)
            admin.save()
            Member.objects.filter(id=member.id).delete()

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
    context['title'] = 'Create Admin'
    return HttpResponse(template.render(context))

@group_required('admin_group')
def admin_download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="poker_club_users.csv"'

    writer = csv.writer(response)

    members = Member.objects.all()
    admins = Admin.objects.all()
    writer.writerow(['First Name', 'Last Name', 'Email', 'Pokerstars Account', 'Class Year'])
    for admin in admins:
        writer.writerow([admin.user.first_name, admin.user.last_name, admin.user.email, admin.pokerstars_username, admin.class_year_num])
    for member in members:
        writer.writerow([member.user.first_name, member.user.last_name, member.user.email, member.pokerstars_username, member.class_year_num])

    return response

@group_required('admin_group')
def admin_edit_officers_page(request):
    sorted_admin = Admin.objects.all().order_by('officers_page_order')
    OfficerPageFormSet = modelformset_factory(Admin, form=AdminOfficersPageForm, extra=0)
    if request.method == 'POST':
        form = OfficerPageFormSet(request.POST, queryset=sorted_admin)
        
        if (form.is_valid()):
            form.save()

            return redirect('officers',)
    else:
        form = OfficerPageFormSet(queryset=sorted_admin)
        
    context = RequestContext(request)
    titles = [admin.full_name() for admin in sorted_admin]
    for f, name in zip(form, titles):
        f.title = name
    context['forms'] = form
    if (form.errors):
        context['errors'] = True
    template = loader.get_template('users/admin/edit_officers_page.html')
    context['title'] = 'Edit Officers Page'

    return HttpResponse(template.render(context))
