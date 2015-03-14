# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0013_remove_zeltlagerdurchgang_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='address',
            field=models.ForeignKey(default=None, to='zeltlager_registration.Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participant',
            name='zeltlager_durchgang',
            field=models.ForeignKey(default=None, to='zeltlager_registration.ZeltlagerDurchgang'),
            preserve_default=True,
        ),
    ]
