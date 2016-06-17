# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0015_volunteer_ngo_request_additional_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activityname', models.TextField(default=b'', max_length=240)),
                ('skill_science', models.BooleanField(default=False)),
                ('skill_math', models.BooleanField(default=False)),
                ('skill_english', models.BooleanField(default=False)),
                ('skill_ict', models.BooleanField(default=False)),
                ('skill_programming', models.BooleanField(default=False)),
                ('skill_socialmediamarket', models.BooleanField(default=False)),
                ('skill_sport', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recurring_request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.TextField(max_length=20)),
                ('recepient', models.TextField(max_length=20)),
                ('startdate_vol', models.DateField(blank=True)),
                ('enddate_vol', models.DateField(blank=True)),
                ('time_vol', models.TimeField(blank=True)),
                ('activity', models.TextField(default=b'', max_length=240)),
                ('frequency', models.TextField(default=b'', max_length=240)),
                ('date_time_req', models.DateTimeField(auto_now_add=True)),
                ('vol_duration', models.IntegerField(default=0)),
                ('status', models.TextField(default=b'Pending')),
            ],
        ),
        migrations.RemoveField(
            model_name='volunteer_ngo_request',
            name='additional_details',
        ),
        migrations.RemoveField(
            model_name='volunteer_ngo_request',
            name='date_time_vol',
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='activity',
            field=models.TextField(default=b'', max_length=240),
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='date_vol',
            field=models.DateField(default=datetime.date(2016, 6, 14)),
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='feedback_ngo',
            field=models.TextField(default=b'', max_length=240, blank=True),
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='feedback_ngorating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='feedback_user',
            field=models.TextField(default=b'', max_length=240, blank=True),
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='feedback_userrating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='onetime',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 14, 9, 48, 23, 858000)),
        ),
    ]
