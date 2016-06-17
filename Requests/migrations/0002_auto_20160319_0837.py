# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer_ngo_request',
            old_name='date_time',
            new_name='date_time_vol',
        ),
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='status',
            field=models.TextField(default=b'Pending'),
        ),
    ]
