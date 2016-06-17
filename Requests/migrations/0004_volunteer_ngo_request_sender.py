# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0003_remove_volunteer_ngo_request_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer_ngo_request',
            name='sender',
            field=models.TextField(default='sjoshi804', max_length=20),
            preserve_default=False,
        ),
    ]
