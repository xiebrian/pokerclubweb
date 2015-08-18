from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
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
    return '/'.join(['profile_pictures', str(instance.id), filename])

def sponsor_logo_file_name(instance, filename):
    return '/'.join(['sponsor_logos', str(instance.id), filename])

def resume_file_name(instance, filename):
    return '/'.join(['resumes', str(instance.id), filename])

def pdf_file(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension, must be one of these file types: ' + str(valid_extensions))

class Student(models.Model):
    user = models.OneToOneField(User)
    resume = models.FileField(blank=True, upload_to=resume_file_name, validators=[pdf_file])
    pokerstars_username = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, upload_to=profile_picture_file_name)
    bio = models.TextField(blank=True)
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
    class_year = models.CharField(max_length=2,
                                      choices=CLASS_YEAR_CHOICES,
                                      default=FRESHMAN)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return '/static/frontend/img/profile_default.png'

    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        abstract=True


class Member(Student):
    is_registered = models.BooleanField(default=False)

class Admin(Student):
    position = models.CharField(max_length=100)

    def update_with_member(self, member):
        self.user = member.user
        self.resume = member.resume
        self.picture = member.picture
        self.bio = member.bio
        self.is_member = True
        self.class_year = member.class_year

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
            return '/static/frontend/img/profile_default.png'

    def can_view_resumes(self):
        return self.level in [self.PLATINUM, self.GOLD]

