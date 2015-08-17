# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('places', models.PositiveSmallIntegerField()),
                ('location', models.CharField(max_length=500)),
                ('results_available', models.BooleanField(default=False)),
                ('registered_members', models.ManyToManyField(to='users.Member', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.PositiveSmallIntegerField()),
                ('member', models.ForeignKey(blank=True, to='users.Member', null=True)),
                ('tournament', models.ForeignKey(to='tournaments.Tournament')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tournamentresult',
            unique_together=set([('tournament', 'member'), ('tournament', 'place')]),
        ),
    ]
