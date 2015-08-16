# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_auto_20150816_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentresult',
            name='student',
            field=models.ForeignKey(blank=True, to='users.Student', null=True),
        ),
    ]
