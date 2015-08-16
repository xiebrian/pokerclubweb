# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150816_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(default=b'img/profile_default.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.URLField(blank=True),
        ),
    ]
