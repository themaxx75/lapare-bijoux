# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20151021_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expo',
            old_name='location',
            new_name='adresse',
        ),
        migrations.AddField(
            model_name='vente',
            name='adresse',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vente',
            name='nom',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vente',
            name='url',
            field=models.URLField(null=True, default=None),
        ),
    ]
