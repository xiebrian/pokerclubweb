from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)