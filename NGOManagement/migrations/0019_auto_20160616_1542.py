# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0018_auto_20160616_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='sender',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 16, 15, 42, 43, 326000)),
        ),
    ]
