# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0026_auto_20160615_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='activity_goal',
            field=models.TextField(max_length=240, null=True),
        ),
        migrations.RemoveField(
            model_name='events',
            name='activities',
        ),
        migrations.AddField(
            model_name='events',
            name='activities',
            field=models.ManyToManyField(to='Requests.Activity'),
        ),
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 11, 45, 16, 734000)),
        ),
    ]
