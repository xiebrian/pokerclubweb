# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20151111_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='class_year_num',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='class_year_num',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='pokerstars_username',
            field=models.CharField(max_length=100, verbose_name=b'Username', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='pokerstars_username',
            field=models.CharField(max_length=100, verbose_name=b'Username', blank=True),
        ),
    ]
