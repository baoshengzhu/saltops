# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 07:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deploy_manager', '0042_auto_20170220_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='backup_monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backup_monitor', to=settings.AUTH_USER_MODEL, verbose_name='备份负责人'),
        ),
        migrations.AddField(
            model_name='project',
            name='dev_monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dev_monitor', to=settings.AUTH_USER_MODEL, verbose_name='开发负责人'),
        ),
        migrations.AddField(
            model_name='project',
            name='ops_monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ops_monitor', to=settings.AUTH_USER_MODEL, verbose_name='运维负责人'),
        ),
    ]
