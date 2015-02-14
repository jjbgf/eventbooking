# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0006_auto_20150214_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='gender',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
