# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_auto_20160227_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(verbose_name=b'created'),
        ),
        migrations.AlterField(
            model_name='car',
            name='modified',
            field=models.DateTimeField(verbose_name=b'modified'),
        ),
    ]
