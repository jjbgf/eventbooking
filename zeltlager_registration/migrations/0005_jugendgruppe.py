# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeltlager_registration', '0004_merge'),
    ]

    operations = [
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
    ]
