# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20151021_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='url',
            field=models.URLField(default=None, blank=True),
        ),
    ]
