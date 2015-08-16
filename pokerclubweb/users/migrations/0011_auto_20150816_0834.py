# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20150816_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, upload_to=users.models.resume_file_name, validators=[users.models.pdf_file]),
        ),
    ]
