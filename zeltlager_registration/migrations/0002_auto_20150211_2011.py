# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugendgruppe',
            name='address',
        ),
        migrations.DeleteModel(
            name='Jugendgruppe',
        ),
        migrations.RemoveField(
            model_name='zeltlagerdurchgang',
            name='address',
        ),
        migrations.RemoveField(
            model_name='zeltlagerdurchgang',
            name='description',
        ),
    ]
