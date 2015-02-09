# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=200)),
                ('street_additional', models.CharField(max_length=10)),
                ('street_number', models.PositiveIntegerField()),
                ('postcode', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=200)),
                ('bundesland', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jugendgruppe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('address', models.ForeignKey(default=None, blank=True, to='zeltlager_registration.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200, blank=True)),
                ('mobile_number', models.CharField(max_length=200, blank=True)),
                ('jugendgruppe', models.CharField(max_length=200, blank=True)),
                ('mail', models.EmailField(max_length=254, blank=True)),
                ('job', models.CharField(max_length=200, blank=True)),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=200)),
                ('vegetarian', models.BooleanField(default=False)),
                ('restrictions', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('legal_guardian', models.CharField(max_length=200)),
                ('legal_guardian_phone_number', models.CharField(max_length=200)),
                ('legal_guardian_mobile_number', models.CharField(max_length=200)),
                ('insurance_company', models.CharField(max_length=200)),
                ('insurance_number', models.PositiveIntegerField()),
                ('main_insurant', models.CharField(max_length=200)),
                ('main_insurant_birthdate', models.DateField()),
                ('main_insurant_address', models.CharField(max_length=200)),
                ('main_insurant_employer', models.CharField(max_length=200)),
                ('tetanus_immunization', models.DateField(null=True, blank=True)),
                ('remember_me_about_medicine', models.TextField(blank=True)),
                ('swimming_badge', models.CharField(max_length=200, blank=True)),
                ('allow_separation_in_groups', models.BooleanField(default=False)),
                ('additional_participants_same_household', models.CharField(max_length=200, blank=True)),
                ('partial_participant', models.BooleanField(default=False)),
                ('partial_start', models.DateField(null=True, blank=True)),
                ('partial_end', models.DateField(null=True, blank=True)),
                ('preferred_work', models.TextField(blank=True)),
                ('activities_i_liked', models.TextField(blank=True)),
                ('things_i_can_provide', models.TextField(blank=True)),
                ('arrival_by', models.CharField(max_length=200)),
                ('address', models.ForeignKey(default=None, blank=True, to='zeltlager_registration.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZeltlagerDurchgang',
            fields=[
                ('number', models.IntegerField(serialize=False, primary_key=True)),
                ('place', models.CharField(max_length=200)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('lagerleiter', models.CharField(max_length=200)),
                ('address', models.ForeignKey(default=None, blank=True, to='zeltlager_registration.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='participant',
            name='alternative_zeltlager_durchgang',
            field=models.ForeignKey(related_name='+', default=None, blank=True, to='zeltlager_registration.ZeltlagerDurchgang', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant',
            name='zeltlager_durchgang',
            field=models.ForeignKey(default=None, blank=True, to='zeltlager_registration.ZeltlagerDurchgang', null=True),
            preserve_default=True,
        ),
    ]
