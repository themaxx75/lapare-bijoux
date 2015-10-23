# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0008_bijoux_processed_path'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bijoux',
            options={'verbose_name_plural': 'bijoux'},
        ),
        migrations.AlterField(
            model_name='vente',
            name='url',
            field=models.URLField(max_length=1024, default=None, blank=True),
        ),
    ]
