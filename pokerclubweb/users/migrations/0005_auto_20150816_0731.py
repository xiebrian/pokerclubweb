# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150814_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='name',
            new_name='company_name',
        ),
    ]
