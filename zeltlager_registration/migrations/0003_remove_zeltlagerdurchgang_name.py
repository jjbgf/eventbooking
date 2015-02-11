# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0002_auto_20150211_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zeltlagerdurchgang',
            name='name',
        ),
    ]
