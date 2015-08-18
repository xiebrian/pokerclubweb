# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_tournament_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='registration_open',
            field=models.BooleanField(default=False),
        ),
    ]
