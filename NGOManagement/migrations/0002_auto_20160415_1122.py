# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Donations',
            new_name='Offline_Donations',
        ),
        migrations.RenameModel(
            old_name='ManualVolReq',
            new_name='Offline_VolReq',
        ),
    ]
