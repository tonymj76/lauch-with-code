# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-01 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins_a', '0005_auto_20180324_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='email_address',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='join',
            name='first_name',
            field=models.CharField(max_length=129, verbose_name='Name'),
        ),
    ]
