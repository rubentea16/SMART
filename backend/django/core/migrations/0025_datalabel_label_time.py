# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20171030_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalabel',
            name='label_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
