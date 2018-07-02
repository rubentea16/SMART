# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-29 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_merge_20180628_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='datauncertainty',
            name='qbc',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='project',
            name='learning_method',
            field=models.CharField(choices=[('least confident', 'By Uncertainty using Least Confident'), ('margin sampling', 'By Uncertainty using the Margin'), ('entropy', 'By Uncertainty using Entropy'), ('random', 'Randomly (No Active Learning)'), ('qbc', 'Query by Committee (using bagging)')], default='least confident', max_length=15),
        ),
    ]
