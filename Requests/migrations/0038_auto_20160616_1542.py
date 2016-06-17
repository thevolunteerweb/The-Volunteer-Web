# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0037_auto_20160616_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_name',
            field=models.TextField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='projects',
            name='project_name',
            field=models.TextField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 16, 15, 42, 43, 311000)),
        ),
    ]
