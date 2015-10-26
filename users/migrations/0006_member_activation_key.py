# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150901_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
