import os
from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def filename(file):
    return os.path.basename(file.name)