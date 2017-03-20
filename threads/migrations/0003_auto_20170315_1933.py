# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20170311_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 15, 19, 33, 58, 671790, tzinfo=utc)),
        ),
    ]
