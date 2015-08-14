# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150814_0601'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.PositiveSmallIntegerField()),
                ('student', models.ForeignKey(to='users.Student')),
                ('tournament', models.ForeignKey(to='tournaments.Tournament')),
            ],
        ),
        migrations.RemoveField(
            model_name='tournamentresults',
            name='student',
        ),
        migrations.RemoveField(
            model_name='tournamentresults',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='TournamentResults',
        ),
    ]
