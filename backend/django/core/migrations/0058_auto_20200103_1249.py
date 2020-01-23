# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-01-03 12:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0057_merge_20191231_1846"),
    ]

    operations = [
        migrations.RemoveField(model_name="projectmetadata", name="id",),
        migrations.AlterField(
            model_name="projectmetadata",
            name="project",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="core.Project",
            ),
        ),
    ]