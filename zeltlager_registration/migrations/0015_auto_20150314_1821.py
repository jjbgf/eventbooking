# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0014_auto_20150314_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='bundesland',
            new_name='state',
        ),
    ]
