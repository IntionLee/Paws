# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 11:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0008_auto_20170307_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylostnotice',
            name='poster',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
