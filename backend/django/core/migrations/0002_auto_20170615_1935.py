# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="model", name="pickle_path", field=models.TextField(),
        ),
    ]
