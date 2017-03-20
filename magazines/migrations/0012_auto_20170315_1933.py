# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0011_auto_20170311_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 15, 19, 33, 58, 596847, tzinfo=utc)),
        ),
    ]
