from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def place_color(place):
    colors = {
    	1: 'yellow',
    	2: 'grey',
    	3: 'brown',
    }
    if place in colors.keys():
    	return colors[place]
    else:
    	return 'blue'