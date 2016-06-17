# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0036_auto_20160615_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='date_vol',
            field=models.DateField(default=datetime.date(2016, 6, 16)),
        ),
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 16, 12, 5, 24, 715000)),
        ),
    ]
