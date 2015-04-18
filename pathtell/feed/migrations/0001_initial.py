# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.BooleanField()),
                ('condition', models.CharField(max_length=30)),
                ('timestamp', models.CharField(max_length=30)),
                ('event_graph', models.CharField(max_length=100000)),
            ],
        ),
        migrations.AddField(
            model_name='alert',
            name='event',
            field=models.ForeignKey(to='feed.Event'),
        ),
    ]
