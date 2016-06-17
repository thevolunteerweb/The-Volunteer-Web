# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0020_auto_20160614_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_req', models.DateTimeField(auto_now_add=True)),
                ('organizer', models.TextField(max_length=20)),
                ('startdate_vol', models.DateField(blank=True)),
                ('enddate_vol', models.DateField(blank=True)),
                ('starttime_vol', models.TimeField(blank=True)),
                ('endtime_vol', models.TimeField(blank=True)),
                ('activities', models.TextField(default=b'', max_length=240)),
                ('feedback_user', models.TextField(default=b'', max_length=240, blank=True)),
                ('feedback_ngo', models.TextField(default=b'', max_length=240, blank=True)),
                ('feedback_userrating', models.IntegerField(default=0)),
                ('feedback_ngorating', models.IntegerField(default=0)),
                ('status', models.TextField(default=b'Upcoming')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_req', models.DateTimeField(auto_now_add=True)),
                ('organizer', models.TextField(max_length=20)),
                ('startdate_vol', models.DateField(blank=True)),
                ('enddate_vol', models.DateField(blank=True)),
                ('starttime_vol', models.TimeField(blank=True)),
                ('endtime_vol', models.TimeField(blank=True)),
                ('activities', models.TextField(default=b'', max_length=240)),
                ('feedback_user', models.TextField(default=b'', max_length=240, blank=True)),
                ('feedback_ngo', models.TextField(default=b'', max_length=240, blank=True)),
                ('feedback_userrating', models.IntegerField(default=0)),
                ('feedback_ngorating', models.IntegerField(default=0)),
                ('status', models.TextField(default=b'Upcoming')),
            ],
        ),
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='date_vol',
            field=models.DateField(default=datetime.date(2016, 6, 15)),
        ),
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 6, 4, 3, 722000)),
        ),
    ]
