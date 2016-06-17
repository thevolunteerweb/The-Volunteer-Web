# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGOManagement', '0003_auto_20160415_1711'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Offline_Vol',
        ),
    ]
