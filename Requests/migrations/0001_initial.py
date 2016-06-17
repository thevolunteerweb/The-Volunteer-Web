# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer_ngo_request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.TextField(max_length=20)),
                ('recepient', models.TextField(max_length=20)),
                ('date_time', models.DateTimeField(blank=True)),
                ('additional_details', models.TextField(max_length=240, blank=True)),
            ],
        ),
    ]
