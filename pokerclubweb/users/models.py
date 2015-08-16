from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from api.models import Project
student_group, created = Group.objects.get_or_create(name='student_group')
admin_group, created = Group.objects.get_or_create(name='admin_group')
sponsor_group, created = Group.objects.get_or_create(name='sponsor_group')

# # Code to add permission to group ???
# ct = ContentType.objects.get_for_model(Project)

# # Now what - Say I want to add 'Can add project' permission to new_group?
# permission = Permission.objects.create(codename='can_add_project',
#                                    name='Can add project',
#                                    content_type=ct)
# new_group.permissions.add(permission)

class Student(models.Model):
    user = models.OneToOneField(User)
    resume = models.URLField()
    picture = models.ImageField()
    bio = models.CharField(max_length=10000)
    is_member = models.BooleanField(default=False)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    CLASS_YEAR_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    class_year = models.CharField(max_length=2,
                                      choices=CLASS_YEAR_CHOICES,
                                      default=FRESHMAN)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Admin(Student):
    position = models.CharField(max_length=100)

class Sponsor(models.Model):
    user = models.OneToOneField(User)
    company_name = models.CharField(max_length=100)
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
        return self.name

