# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmmi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_final_estimada',
            field=models.DateTimeField(blank=True, null=True, verbose_name='fecha de finalizacion estimada'),
        ),
    ]
