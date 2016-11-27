# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import stdnumfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('oib', stdnumfield.models.StdNumField(formats=['hr.oib'])),
            ],
        ),
    ]
