# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins_a', '0003_joinfriends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinfriends',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='Friend', to='joins_a.Join'),
        ),
    ]
