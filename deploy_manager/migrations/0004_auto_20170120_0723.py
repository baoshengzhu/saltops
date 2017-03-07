# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0003_auto_20170120_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to=b'', verbose_name='\u7248\u672c\u6587\u4ef6')),
            ],
            options={
                'verbose_name': '\u7248\u672c\u6587\u4ef6',
                'verbose_name_plural': '\u7248\u672c\u6587\u4ef6',
            },
        ),
        migrations.RemoveField(
            model_name='projectversion',
            name='files',
        ),
        migrations.AddField(
            model_name='projectfiles',
            name='project_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.ProjectVersion', verbose_name='\u7248\u672c\u4fe1\u606f'),
        ),
    ]