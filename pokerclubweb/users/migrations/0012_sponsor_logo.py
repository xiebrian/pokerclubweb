# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150816_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(default='img/profile_default.png', upload_to=users.models.sponsor_logo_file_name),
            preserve_default=False,
        ),
    ]
