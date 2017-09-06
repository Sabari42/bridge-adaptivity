# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridge_lti', '0009_auto_20170822_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutcomeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lis_outcome_service_url', models.CharField(max_length=255)),
                ('lms_lti_connection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bridge_lti.LtiProvider')),
            ],
            options={
                'verbose_name': 'outcome service',
                'verbose_name_plural': 'outcome services',
            },
        ),
    ]
