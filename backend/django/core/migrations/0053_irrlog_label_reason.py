# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-12-10 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_datalabel_label_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='irrlog',
            name='label_reason',
            field=models.TextField(default=''),
        ),
    ]
