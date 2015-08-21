from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

@register.filter
def are_level(sponsors, level_name):
    return sponsors.filter(level=level_name)
