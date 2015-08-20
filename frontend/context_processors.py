from django.contrib.sites.models import get_current_site
from django.utils.functional import SimpleLazyObject


def frontend(request):
    """
    Additional variables to include in *every* template.
    """
    site = SimpleLazyObject(lambda: get_current_site(request))
    http_scheme = 'https://' if request.is_secure() else 'http://'

    return {
        'site': site,
        'site_root': SimpleLazyObject(lambda: "{0}{1}".format(http_scheme, site.domain)),
    }

def icons(request):
    icons_map = {
        'username': 'user',
        'password': 'lock',
        'password1': 'lock',
        'password2': 'lock',
        'old_password': 'lock',
        'new_password1': 'lock',
        'new_password2': 'lock',
        'first_name': 'tag',
        'last_name': 'tag',
        'email': 'mail',
        'member': 'users',
        'resume': 'file pdf outline',
        'pokerstars_username': 'spy',
        'picture': 'photo',
        #'bio': 'book',
        'class_year': 'student',
        'position': 'building',
        'company_name': 'suitcase',
        'logo': 'photo',
        'home_page_url': 'linkify',
        'level': 'money',
        'name': 'tag',
        'start_time': 'calendar',
        'end_time': 'calendar',
        #'description': 'newspaper',
        'registered_members': 'users',
        'places': 'trophy',
        'location': 'marker',
        'registration_open': 'unlock alternate',
        'results_available': 'unhide',
    }
    return { 'icons' : icons_map }