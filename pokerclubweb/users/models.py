from django.db import models
from django.contrib.auth.models import User
import datetime from datetime

class Student(models.Model):
    user = models.OneToOneField(User)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    classyear = models.IntegerField(validators=[validate_class_year])
    resume = models.URLField()
    picture = models.ImageField()


def validate_class_year(value):
    now = datetime.now()
    minyear = now.year
    maxyear = now.year + 3
    if (now.month > 6):
        minyear = minyear + 1
        maxyear = maxyear + 1

    if (value < minyear or value > maxyear):
        raise ValidationError('%s is not a valid class year' % value)

