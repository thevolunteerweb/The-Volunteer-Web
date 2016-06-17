# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0002_auto_20160415_1122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offline_VolReq',
            new_name='Offline_Vol',
        ),
    ]
