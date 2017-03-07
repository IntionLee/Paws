# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20170228_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyLostNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petimg', models.ImageField(upload_to='image/%Y/%m/%d/')),
                ('animal', models.CharField(max_length=50)),
                ('pettype', models.CharField(max_length=50)),
                ('petid', models.CharField(max_length=50)),
                ('petcolor', models.CharField(max_length=50)),
                ('petfeature', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=50)),
                ('time', models.DateField()),
                ('contactname', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
