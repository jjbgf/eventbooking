# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0008_auto_20150214_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='bundesland',
            field=models.CharField(max_length=100, choices=[(b'BW', 'Baden-Wuerttemberg'), (b'BY', 'Bavaria'), (b'BE', 'Berlin'), (b'BB', 'Brandenburg'), (b'HB', 'Bremen'), (b'HH', 'Hamburg'), (b'HE', 'Hessen'), (b'MV', 'Mecklenburg-Western Pomerania'), (b'NI', 'Lower Saxony'), (b'NW', 'North Rhine-Westphalia'), (b'RP', 'Rhineland-Palatinate'), (b'SL', 'Saarland'), (b'SN', 'Saxony'), (b'ST', 'Saxony-Anhalt'), (b'SH', 'Schleswig-Holstein'), (b'TH', 'Thuringia')]),
            preserve_default=True,
        ),
    ]
