# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0019_auto_20160614_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='ngo_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 14, 22, 1, 52, 397000)),
        ),
    ]
