# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmmi', '0002_auto_20170730_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='porcentaje_completado',
            new_name='porcentage_completado',
        ),
    ]
