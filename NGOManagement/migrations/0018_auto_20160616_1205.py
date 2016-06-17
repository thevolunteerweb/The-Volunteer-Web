# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0017_auto_20160615_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='status',
            field=models.TextField(default=b'Pending', max_length=240),
        ),
        migrations.AlterField(
            model_name='offline_donations',
            name='date_donated',
            field=models.DateField(default=datetime.date(2016, 6, 16)),
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='date_vol',
            field=models.DateField(default=datetime.date(2016, 6, 16)),
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 16, 12, 5, 24, 730000)),
        ),
    ]
