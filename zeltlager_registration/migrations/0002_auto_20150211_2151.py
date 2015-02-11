# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street_additional',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
