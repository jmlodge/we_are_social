# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20170315_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 19, 48, 35, 266686, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='subject',
            field=models.ForeignKey(related_name='threads', to='threads.Subject'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='user',
            field=models.ForeignKey(related_name='threads', to=settings.AUTH_USER_MODEL),
        ),
    ]
