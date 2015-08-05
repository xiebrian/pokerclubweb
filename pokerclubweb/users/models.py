from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User)
    resume = models.URLField()
    picture = models.ImageField()
    bio = models.CharField(max_length=10000)
    isMember = models.BooleanField(default=False)
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
    classyear = models.CharField(max_length=2,
                                      choices=CLASS_YEAR_CHOICES,
                                      default=FRESHMAN)

class Admin(Student):
    position = models.CharField(max_length=100)

class Sponsor(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    BRONZE = 'BR'
    SILVER = 'SL'
    GOLD = 'GD'
    PLATINUM = 'PL'
    LEVEL_CHOICES = (
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
        (PLATINUM, 'PLATINUM')
    )
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        default=BRONZE
    )