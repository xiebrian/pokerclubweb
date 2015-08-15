# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20150814_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='TournamentName', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='location',
            field=models.CharField(max_length=500),
        ),
    ]
