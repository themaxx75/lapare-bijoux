# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0009_auto_20151022_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='expo',
            name='info_url',
            field=models.URLField(blank=True, null=True, max_length=1024, default=None),
        ),
    ]
