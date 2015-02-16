# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0010_auto_20150216_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street_additional',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
