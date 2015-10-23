# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_vente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vente',
            name='province',
            field=models.IntegerField(choices=[(1, 'Alberta'), (2, 'Colombie-Britannique'), (3, 'Manitoba'), (4, 'Nouveau-Brunswick'), (5, 'Nouvelle-Écosse'), (6, 'Nunavut'), (7, 'Ontario'), (8, 'Québec'), (9, 'Saskatchewan'), (10, 'Terre-Neuve-et-Labrador'), (11, 'Territoires du Nord-Ouest'), (12, 'Yukon'), (13, 'Île-du-Prince-Édouard')]),
        ),
    ]
