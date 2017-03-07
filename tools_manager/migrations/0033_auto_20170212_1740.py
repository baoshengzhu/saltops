# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools_manager', '0032_auto_20170212_1709'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToolsExecHistory',
            new_name='ToolsExecJob',
        ),
        migrations.AlterField(
            model_name='toolsexecjob',
            name='tools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsScript', verbose_name='工具'),
        ),
        migrations.AlterField(
            model_name='toolsscript',
            name='tools_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsTypes', verbose_name='工具类型'),
        ),
    ]