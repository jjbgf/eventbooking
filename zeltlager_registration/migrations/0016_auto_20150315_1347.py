# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0015_auto_20150314_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='arrival_by',
        ),
        migrations.AddField(
            model_name='participant',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 12, 47, 18, 971000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 12, 47, 27, 807000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='transportationBegin',
            field=models.CharField(default=datetime.datetime(2015, 3, 15, 12, 47, 34, 345000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='transportationBeginMethod',
            field=models.CharField(default=b'keine', max_length=20, choices=[(b'KFZ_Eigen', b'Eigenes KFZ'), (b'KFZ_mitfahrt', b'Mitfahrer'), (b'BusSMH', b'Bus ab SMH'), (b'BusFS', b'Bus ab FS'), (b'Bahn', b'Bahn'), (b'Flugzeug', b'Flugzeug'), (b'zuFuss', b'zu Fuss'), (b'andere', b'andere'), (b'keine', b'keine')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='transportationEnd',
            field=models.CharField(default=datetime.datetime(2015, 3, 15, 12, 47, 42, 178000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='transportationEndMethod',
            field=models.CharField(default=b'keine', max_length=20, choices=[(b'KFZ_Eigen', b'Eigenes KFZ'), (b'KFZ_mitfahrt', b'Mitfahrer'), (b'BusSMH', b'Bus ab SMH'), (b'BusFS', b'Bus ab FS'), (b'Bahn', b'Bahn'), (b'Flugzeug', b'Flugzeug'), (b'zuFuss', b'zu Fuss'), (b'andere', b'andere'), (b'keine', b'keine')]),
            preserve_default=True,
        ),
    ]
