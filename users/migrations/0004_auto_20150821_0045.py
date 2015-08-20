# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150818_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='bio',
            field=models.TextField(default=b'I <3 Poker'),
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(default=b'I <3 Poker'),
        ),
    ]
