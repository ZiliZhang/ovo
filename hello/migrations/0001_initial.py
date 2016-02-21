# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-21 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('birth_date', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
