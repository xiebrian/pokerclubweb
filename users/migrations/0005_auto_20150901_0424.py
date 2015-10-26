# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150821_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='pokerstars_username',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='pokerstars_username',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
