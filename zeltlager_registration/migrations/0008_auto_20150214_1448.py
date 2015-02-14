# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0007_participant_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(max_length=10, choices=[(b'0', b'weiblich'), (b'1', b'm\xc3\xa4nnlich')]),
            preserve_default=True,
        ),
    ]
