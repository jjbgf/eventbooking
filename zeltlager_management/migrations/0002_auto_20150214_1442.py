# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Buchung', 'verbose_name_plural': 'Buchungen'},
        ),
        migrations.AddField(
            model_name='booking',
            name='transportationBeginMethod',
            field=models.CharField(default=b'keine', max_length=20, choices=[(b'KFZ_Eigen', b'Eigenes KFZ'), (b'KFZ_mitfahrt', b'Mitfahrer'), (b'BusSMH', b'Bus ab SMH'), (b'BusFS', b'Bus ab FS'), (b'Bahn', b'Bahn'), (b'Flugzeug', b'Flugzeug'), (b'zuFuss', b'zu Fuss'), (b'andere', b'andere'), (b'keine', b'keine')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='transportationEndMethod',
            field=models.CharField(default=b'keine', max_length=20, choices=[(b'KFZ_Eigen', b'Eigenes KFZ'), (b'KFZ_mitfahrt', b'Mitfahrer'), (b'BusSMH', b'Bus ab SMH'), (b'BusFS', b'Bus ab FS'), (b'Bahn', b'Bahn'), (b'Flugzeug', b'Flugzeug'), (b'zuFuss', b'zu Fuss'), (b'andere', b'andere'), (b'keine', b'keine')]),
            preserve_default=True,
        ),
    ]
