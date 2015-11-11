# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_admin_officer_page_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='officer_page_order',
            new_name='officers_page_order',
        ),
    ]
