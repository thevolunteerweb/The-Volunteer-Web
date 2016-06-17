# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0028_auto_20160615_1246'),
        ('Registration', '0014_userprofile_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoprofile',
            name='activity',
            field=models.ManyToManyField(to='Requests.Activity'),
        ),
    ]
