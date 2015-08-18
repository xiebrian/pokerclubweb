# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150817_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='pokerstars_username',
            field=models.CharField(default='pokerstar101', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='pokerstars_username',
            field=models.CharField(default='pokerstar101', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='class_year',
            field=models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior'), (b'GR', b'Graduate')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='class_year',
            field=models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior'), (b'GR', b'Graduate')]),
        ),
    ]
