# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0012_volunteer_ngo_request_date_time_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer_ngo_request',
            name='accept',
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='vol_duration',
            field=models.IntegerField(default=0),
        ),
    ]
