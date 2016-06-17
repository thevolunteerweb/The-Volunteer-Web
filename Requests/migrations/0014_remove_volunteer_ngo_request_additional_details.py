# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0013_auto_20160409_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer_ngo_request',
            name='additional_details',
        ),
    ]
