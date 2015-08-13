# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='club',
            field=models.CharField(default=b'BB', max_length=2, choices=[(b'BB', b'Basketball'), (b'BA', b'Badminton')]),
        ),
    ]
