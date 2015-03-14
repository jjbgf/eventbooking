# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_management', '0002_auto_20150214_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(default=None, to='zeltlager_registration.ZeltlagerDurchgang'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='booking',
            name='participant',
            field=models.ForeignKey(default=None, to='zeltlager_registration.Participant'),
            preserve_default=True,
        ),
    ]
