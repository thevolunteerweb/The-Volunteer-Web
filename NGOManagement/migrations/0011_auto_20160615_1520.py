# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0010_auto_20160615_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='offline_donations',
            name='date_donated',
            field=models.DateField(default=datetime.date(2016, 6, 15)),
        ),
        migrations.AddField(
            model_name='offline_donations',
            name='mode_of_payment',
            field=models.TextField(default=b'Not Specified', max_length=30),
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 15, 20, 28, 954000)),
        ),
    ]
