# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 03:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160929_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbuddy',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userbuddy', to=settings.AUTH_USER_MODEL),
        ),
    ]
