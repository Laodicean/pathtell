# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_graph',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
