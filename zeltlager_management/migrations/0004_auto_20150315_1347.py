# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_management', '0003_auto_20150314_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='arrival',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='transportationBegin',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='transportationBeginMethod',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='transportationEnd',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='transportationEndMethod',
        ),
    ]
