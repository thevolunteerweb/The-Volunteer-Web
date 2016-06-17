# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0005_offline_vol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offline_vol',
            name='feedback_ngo',
        ),
        migrations.RemoveField(
            model_name='offline_vol',
            name='feedback_ngorating',
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 10, 18, 49, 22000)),
        ),
    ]
