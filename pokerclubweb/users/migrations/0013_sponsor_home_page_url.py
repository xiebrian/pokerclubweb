# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_sponsor_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='home_page_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
