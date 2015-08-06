# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
            bases=('auth.group',),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='level',
            field=models.CharField(default=b'BR', max_length=2, choices=[(b'BR', b'Bronze'), (b'SL', b'Silver'), (b'GD', b'Gold'), (b'PL', b'Platinum')]),
        ),
    ]
