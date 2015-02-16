# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0011_auto_20150216_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zeltlagerdurchgang',
            name='place',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
