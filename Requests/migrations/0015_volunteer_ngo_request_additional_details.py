# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0014_remove_volunteer_ngo_request_additional_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='additional_details',
            field=models.TextField(default=b'N/A', max_length=240, blank=True),
        ),
    ]
