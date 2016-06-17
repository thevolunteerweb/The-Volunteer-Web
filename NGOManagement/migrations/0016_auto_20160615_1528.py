# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0015_auto_20160615_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offline_donations',
            name='mode_of_payment',
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 15, 28, 1, 771000)),
        ),
    ]
