# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-30 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_auto_20180316_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='repetition',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sequenceitem',
            name='suffix',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
