# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('first_name', models.CharField(max_length=129)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('ip_address', models.GenericIPAddressField(default='1.1.1')),
                ('ref_address', models.CharField(default='ABC', max_length=122)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('id_join', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-created_date', '-update_date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email_address', 'ref_address')]),
        ),
    ]
