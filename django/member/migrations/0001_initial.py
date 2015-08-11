# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('chinese_name', models.CharField(max_length=60, blank=True)),
                ('english_name', models.CharField(max_length=60, blank=True)),
                ('email', models.EmailField(max_length=60, blank=True)),
                ('phone', models.CharField(max_length=160, null=True, blank=True)),
                ('club', models.CharField(default=b'BB', max_length=2, choices=[(b'BB', b'Basketball'), (b'VO', b'Volleyball')])),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=4)),
                ('member', models.ForeignKey(to='member.Member')),
            ],
        ),
    ]
