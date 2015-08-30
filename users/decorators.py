from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.utils.functional import wraps
from django.conf import settings

# def can_view_resumes(user):
#     if user.groups.filter(group='admin_group').exists():
#         return True
#     elif user.sponsor:
#         return user.sponsor.can_view_resumes()
#     return False

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)

def is_self_or_admin(view):
    @wraps(view)
    def inner(request, userID, *args, **kwargs):
        if str(request.user.id) != userID and not request.user.groups.filter(name='admin_group').exists():
            return redirect('login')

        return view(request, userID, *args, **kwargs)
    return inner

def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = 'index'

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous(),
        login_url=redirect_url,
        redirect_field_name=None
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

def can_view_resumes(view):
    @wraps(view)
    def inner(request, userID, *args, **kwargs):
        if str(request.user.id) != userID \
            and not request.user.groups.filter(name='admin_group').exists() \
            and not request.user.groups.filter(name='sponsor_group').exists():
            return redirect('profile', userID=userID)

        return view(request, userID, *args, **kwargs)
    return inner