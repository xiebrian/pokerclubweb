# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150816_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
