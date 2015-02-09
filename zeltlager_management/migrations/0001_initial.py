# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('arrival', models.DateTimeField()),
                ('departure', models.DateTimeField()),
                ('comment', models.CharField(max_length=500, blank=True)),
                ('transportationBegin', models.CharField(max_length=20)),
                ('transportationEnd', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('hasPaid', models.BooleanField(default=False)),
                ('isReduced', models.BooleanField(default=False)),
                ('familyMembers', models.IntegerField()),
                ('bookingDate', models.DateTimeField()),
                ('event', models.ForeignKey(default=None, blank=True, to='zeltlager_registration.ZeltlagerDurchgang')),
                ('participant', models.ForeignKey(default=None, blank=True, to='zeltlager_registration.Participant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
