# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joins_a', '0004_auto_20180324_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinfriends',
            name='email',
        ),
        migrations.RemoveField(
            model_name='joinfriends',
            name='email_all',
        ),
        migrations.RemoveField(
            model_name='joinfriends',
            name='friends',
        ),
        migrations.AddField(
            model_name='join',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral', to='joins_a.Join'),
        ),
        migrations.DeleteModel(
            name='JoinFriends',
        ),
    ]
