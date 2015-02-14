# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0005_jugendgruppe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Adresse', 'verbose_name_plural': 'Adressen'},
        ),
        migrations.AlterModelOptions(
            name='jugendgruppe',
            options={'verbose_name': 'Jugendgruppe', 'verbose_name_plural': 'Jugendgruppen'},
        ),
        migrations.AlterModelOptions(
            name='participant',
            options={'verbose_name': 'Teilnehmer', 'verbose_name_plural': 'Teilnehmer'},
        ),
        migrations.AlterModelOptions(
            name='zeltlagerdurchgang',
            options={'verbose_name': 'Zeltlagerdurchgang', 'verbose_name_plural': 'Zeltlagerdurchg\xe4nge'},
        ),
    ]
