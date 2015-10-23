# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0010_expo_info_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expo',
            old_name='info_url',
            new_name='url',
        ),
    ]
