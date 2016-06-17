# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0004_delete_offline_vol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offline_Vol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_req', models.DateTimeField(auto_now_add=True)),
                ('ngo_id', models.TextField(max_length=100)),
                ('volunteer_name', models.TextField(max_length=100, blank=True)),
                ('date_vol', models.DateField(default=datetime.date(2016, 6, 15))),
                ('time_vol', models.TimeField(default=datetime.datetime(2016, 6, 15, 10, 13, 19, 63000))),
                ('hours_vol', models.PositiveSmallIntegerField()),
                ('activity', models.TextField(max_length=100)),
                ('feedback_ngo', models.TextField(default=b'', max_length=240, blank=True)),
                ('feedback_ngorating', models.IntegerField(default=0)),
            ],
        ),
    ]
