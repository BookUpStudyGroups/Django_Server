# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_groups_class1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbuddy',
            name='classes',
            field=models.ManyToManyField(blank=True, to='website.Class'),
        ),
    ]