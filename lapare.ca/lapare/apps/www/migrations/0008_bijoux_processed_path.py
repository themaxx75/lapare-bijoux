# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0007_bijoux_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='bijoux',
            name='processed_path',
            field=models.TextField(default=None, blank=True),
        ),
    ]
