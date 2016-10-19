# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('script_id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('script_name', models.CharField(max_length=128)),
                ('created_date', models.DateTimeField(editable=False)),
                ('modified_date', models.DateTimeField()),
            ],
        ),
    ]
