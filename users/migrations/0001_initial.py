# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resume', models.FileField(blank=True, upload_to=users.models.resume_file_name, validators=[users.models.pdf_file])),
                ('picture', models.ImageField(default=b'img/profile_default.png', upload_to=users.models.profile_picture_file_name)),
                ('bio', models.TextField(blank=True)),
                ('class_year', models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('position', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resume', models.FileField(blank=True, upload_to=users.models.resume_file_name, validators=[users.models.pdf_file])),
                ('picture', models.ImageField(default=b'img/profile_default.png', upload_to=users.models.profile_picture_file_name)),
                ('bio', models.TextField(blank=True)),
                ('class_year', models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('is_registered', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to=users.models.sponsor_logo_file_name)),
                ('home_page_url', models.URLField()),
                ('level', models.CharField(default=b'BR', max_length=2, choices=[(b'BR', b'Bronze'), (b'SL', b'Silver'), (b'GD', b'Gold'), (b'PL', b'Platinum')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
