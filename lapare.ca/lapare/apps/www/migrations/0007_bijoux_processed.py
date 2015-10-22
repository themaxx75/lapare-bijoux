# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_bijoux'),
    ]

    operations = [
        migrations.AddField(
            model_name='bijoux',
            name='processed',
            field=models.TextField(blank=True, default=None),
        ),
    ]
