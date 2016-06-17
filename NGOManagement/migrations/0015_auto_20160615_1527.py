# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0014_auto_20160615_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offline_Donations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ngo_id', models.TextField(max_length=100)),
                ('donor_name', models.TextField(max_length=100, blank=True)),
                ('amount_donated', models.PositiveIntegerField()),
                ('cause', models.TextField(max_length=1000, blank=True)),
                ('mode_of_payment', models.TextField(default=b'Not Specified', max_length=30)),
                ('date_donated', models.DateField(default=datetime.date(2016, 6, 15))),
            ],
        ),
        migrations.AlterField(
            model_name='offline_vol',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 15, 27, 7, 98000)),
        ),
    ]
