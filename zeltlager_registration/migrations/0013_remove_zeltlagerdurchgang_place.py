# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0012_auto_20150216_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zeltlagerdurchgang',
            name='place',
        ),
    ]
