import os
import datetime

from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
from django.conf import settings
# from django.contrib.contenttypes.models import ContentType
# from api.models import Project
# member_group, created = Group.objects.get_or_create(name='member_group')
# admin_group, created = Group.objects.get_or_create(name='admin_group')
# sponsor_group, created = Group.objects.get_or_create(name='sponsor_group')

# # Code to add permission to group ???
# ct = ContentType.objects.get_for_model(Project)

# # Now what - Say I want to add 'Can add project' permission to new_group?
# permission = Permission.objects.create(codename='can_add_project',
#                                    name='Can add project',
#                                    content_type=ct)
# new_group.permissions.add(permission)

def profile_picture_file_name(instance, filename):
    if not filename:
        return '/'.join(['profile_pictures', str(instance.user.id), filename])
    ext = os.path.splitext(filename)[1]
    name = instance.user.first_name + '_' + instance.user.last_name + '_Profile_Picture' + ext
    return '/'.join(['profile_pictures', str(instance.user.id), name])

def sponsor_logo_file_name(instance, filename):
    return '/'.join(['sponsor_logos', str(instance.user.id), filename])

def resume_file_name(instance, filename):
    # if not filename:
    #     return '/'.join(['resumes', str(instance.user.id), filename])
    name = instance.user.first_name + '_' + instance.user.last_name + '_Resume.pdf'
    return '/'.join(['resumes', str(instance.user.id), name])

def pdf_file(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension, must be one of these file types: ' + str(valid_extensions))

class Student(models.Model):
    user = models.OneToOneField(User)
    resume = models.FileField(blank=False, upload_to=resume_file_name, validators=[pdf_file], help_text="Please attach your resume in PDF format.")
    pokerstars_username = models.CharField(max_length=100, blank=True, verbose_name="PokerStars Username", help_text="Required to participate in the SIG Main Event Series. See Join/Contact/FAQ for more info.")
    picture = models.ImageField(blank=True, upload_to=profile_picture_file_name)
    bio = models.TextField(default='I <3 Poker')
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    CLASS_YEAR_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    )

    class_year_num = models.IntegerField(default=datetime.datetime.now().year+4, verbose_name="Undergrad Class Year")
    # class_year = models.CharField(max_length=2,
    #                                  choices=CLASS_YEAR_CHOICES,
    #                                  default=FRESHMAN)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return settings.STATIC_URL+'frontend/img/profile_default.png'

    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        abstract=True


class Member(Student):
    is_registered = models.BooleanField(default=False)
    is_interested_in_exec = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=40, blank=True)

    def results(self):
        return self.tournamentresult_set.all()

class Admin(Student):
    position = models.CharField(max_length=100)
    officers_page_order = models.IntegerField(default=1)

    def update_with_member(self, member):
        for a in member._meta.get_all_field_names():
            setattr(self, a, getattr(member, a, None))
        self.save()

class Sponsor(models.Model):
    user = models.OneToOneField(User)
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=sponsor_logo_file_name)
    home_page_url = models.URLField()
    BRONZE = 'BR'
    SILVER = 'SL'
    GOLD = 'GD'
    PLATINUM = 'PL'
    LEVEL_CHOICES = (
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum')
    )
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        default=BRONZE
    )

    def __unicode__(self):
        return self.company_name

    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return settings.STATIC_URL+'frontend/img/profile_default.png'

    def can_view_resumes(self):
        #return self.level in [self.PLATINUM, self.GOLD]
        return true

