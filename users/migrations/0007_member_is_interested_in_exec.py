# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_member_activation_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_interested_in_exec',
            field=models.BooleanField(default=False),
        ),
    ]
