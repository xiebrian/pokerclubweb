# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0006_auto_20150816_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='results_available',
            field=models.BooleanField(default=False),
        ),
    ]
