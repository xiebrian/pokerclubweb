# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150816_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(default=b'img/profile_default.png', upload_to=users.models.profile_picture_file_name),
        ),
    ]
