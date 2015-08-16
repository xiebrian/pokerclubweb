# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20150816_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='places',
            field=models.PositiveSmallIntegerField(default=3),
            preserve_default=False,
        ),
    ]
