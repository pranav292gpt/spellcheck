# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-17 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20170717_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordfrequency',
            name='frequency',
            field=models.IntegerField(),
        ),
    ]
