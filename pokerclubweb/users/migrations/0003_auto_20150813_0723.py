# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('users', '0002_auto_20150806_0224'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentGroup',
        ),
    ]
