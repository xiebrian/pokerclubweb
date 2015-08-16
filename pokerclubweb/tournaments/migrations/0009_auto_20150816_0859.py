# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_auto_20150816_0855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tournamentresult',
            unique_together=set([('tournament', 'place'), ('tournament', 'student')]),
        ),
    ]
