# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0002_auto_20150207_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='partial_end',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participant',
            name='partial_start',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participant',
            name='tetanus_immunization',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
