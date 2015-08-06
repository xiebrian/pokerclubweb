# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(default=b'BR', max_length=2, choices=[(b'BR', b'Bronze'), (b'SL', b'Silver'), (b'GD', b'Gold'), (b'PL', b'PLATINUM')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resume', models.URLField()),
                ('picture', models.ImageField(upload_to=b'')),
                ('bio', models.CharField(max_length=10000)),
                ('isMember', models.BooleanField(default=False)),
                ('classyear', models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('student_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='users.Student')),
                ('position', models.CharField(max_length=100)),
            ],
            bases=('users.student',),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
