# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0009_auto_20150214_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='position',
            field=models.CharField(blank=True, max_length=20, choices=[(b'Jugendleiter', b'Jugendleiter'), (b'Prediger', b'Prediger'), (b'Hauptjugendleiter', b'Hauptjugendleiter')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='zeltlagerdurchgang',
            name='address',
            field=models.ForeignKey(default=None, blank=True, to='zeltlager_registration.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='zeltlagerdurchgang',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participant',
            name='swimming_badge',
            field=models.CharField(blank=True, max_length=50, choices=[(b'Seepferdchen', b'Seepferdchen'), (b'Bronze', b'Deutsches Jugendschwimmabzeichen \xe2\x80\x93 Bronze'), (b'Silber', b'Deutsches Jugendschwimmabzeichen \xe2\x80\x93 Silber'), (b'Gold', b'Deutsches Jugendschwimmabzeichen \xe2\x80\x93 Gold'), (b'Rettungsschwimmabzeichen', b'Rettungsschwimmabzeichen')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participant',
            name='zeltlager_durchgang',
            field=models.ForeignKey(default=None, blank=True, to='zeltlager_registration.ZeltlagerDurchgang'),
            preserve_default=True,
        ),
    ]
