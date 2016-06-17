# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0013_auto_20160615_1526'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Offline_Donations',
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 15, 26, 45, 448000)),
        ),
    ]
