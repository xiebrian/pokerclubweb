# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_tournament_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
