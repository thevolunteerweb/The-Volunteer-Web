# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ngo_id', models.TextField(max_length=100)),
                ('donor_name', models.TextField(max_length=100, blank=True)),
                ('amount_donated', models.PositiveIntegerField()),
                ('cause', models.TextField(max_length=1000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ngo_id', models.TextField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('purpose', models.TextField(max_length=1000)),
                ('invoice_img', models.ImageField(upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManualVolReq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ngo_id', models.TextField(max_length=100)),
                ('volunteer_name', models.TextField(max_length=100, blank=True)),
                ('hours_vol', models.PositiveSmallIntegerField()),
                ('service_provided', models.TextField(max_length=100)),
            ],
        ),
    ]
