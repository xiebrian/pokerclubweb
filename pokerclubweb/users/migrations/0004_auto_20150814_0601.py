# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150813_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='classyear',
            new_name='class_year',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='isMember',
            new_name='is_member',
        ),
    ]
