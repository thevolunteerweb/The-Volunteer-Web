# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0004_volunteer_ngo_request_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='date_time_req',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 17, 5, 28, 442000), blank=True),
            preserve_default=False,
        ),
    ]
