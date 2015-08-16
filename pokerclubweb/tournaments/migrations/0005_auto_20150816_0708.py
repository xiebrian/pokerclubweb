# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_tournament_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='registered_students',
            field=models.ManyToManyField(to='users.Student', blank=True),
        ),
        migrations.AlterField(
            model_name='tournamentresult',
            name='student',
            field=models.ForeignKey(to='users.Student', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentresult',
            unique_together=set([('tournament', 'place'), ('tournament', 'student')]),
        ),
    ]
