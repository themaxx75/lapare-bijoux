# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_auto_20151021_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bijoux',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
