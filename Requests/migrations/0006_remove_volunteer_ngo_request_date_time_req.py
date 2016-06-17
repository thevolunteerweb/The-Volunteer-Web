# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0005_volunteer_ngo_request_date_time_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer_ngo_request',
            name='date_time_req',
        ),
    ]
