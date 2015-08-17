# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='picture',
            field=models.ImageField(upload_to=users.models.profile_picture_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(upload_to=users.models.profile_picture_file_name, blank=True),
        ),
    ]
