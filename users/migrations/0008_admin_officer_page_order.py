# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_member_is_interested_in_exec'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='officer_page_order',
            field=models.IntegerField(default=1),
        ),
    ]
