# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150813_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.TextField()),
                ('registered_students', models.ManyToManyField(to='users.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.PositiveSmallIntegerField()),
                ('student', models.ForeignKey(to='users.Student')),
                ('tournament', models.ForeignKey(to='tournaments.Tournament')),
            ],
        ),
    ]
