# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmmi', '0004_auto_20170804_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='es_urgente',
            field=models.BooleanField(default=False),
        ),
    ]