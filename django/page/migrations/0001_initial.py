# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_date', models.DateField()),
                ('weekday', models.CharField(max_length=3)),
                ('time_range', models.CharField(max_length=22)),
            ],
        ),
    ]
