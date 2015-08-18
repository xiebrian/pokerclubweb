# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tournaments.models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='picture',
            field=models.ImageField(upload_to=tournaments.models.tournament_picture_file_name, blank=True),
        ),
    ]
