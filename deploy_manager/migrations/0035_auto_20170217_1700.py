# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0034_auto_20170217_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='extra_param',
            field=models.TextField(blank=True, default='', null=True, verbose_name='扩展参数'),
        ),
    ]