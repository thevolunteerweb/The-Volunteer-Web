# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_auto_20160415_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoemployeeprofile',
            name='ngo_id',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='ngoprofile',
            name='ngo_id',
            field=models.TextField(max_length=100, blank=True),
        ),
    ]
