# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160706_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='cr_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
