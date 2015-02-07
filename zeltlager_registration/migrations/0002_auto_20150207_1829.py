# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='activities_i_liked',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='additional_participants_same_household',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='allow_separation_in_groups',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='alternative_zeltlager_durchgang',
            field=models.ForeignKey(related_name='+', default=None, blank=True, to='zeltlager_registration.ZeltlagerDurchgang', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='arrival_by',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 17, 26, 43, 224000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='birth_place',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='bundesland',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='insurance_company',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='insurance_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='job',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='jugendgruppe',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='legal_guardian',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='legal_guardian_mobile_number',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='legal_guardian_phone_number',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='mail',
            field=models.EmailField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='main_insurant',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='main_insurant_address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='main_insurant_birthdate',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 17, 27, 51, 985000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='main_insurant_employer',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='mobile_number',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='partial_end',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 17, 27, 51, 985000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='partial_participant',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='partial_start',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 17, 27, 51, 985000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='phone_number',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='place',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='plz',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='preferred_work',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='remember_me_about_medicine',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='restrictions',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='skills',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='street',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='swimming_badge',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='tetanus_immunization',
            field=models.DateField(default=datetime.datetime(2015, 2, 7, 17, 29, 49, 72000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='things_i_can_provide',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='vegetarian',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
