# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('province', models.TextField(choices=[('AB', 'Alberta'), ('BC', 'Colombie-Britannique'), ('MB', 'Manitoba'), ('NB', 'Nouveau-Brunswick'), ('NS', 'Nouvelle-Écosse'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('QC', 'Québec'), ('SK', 'Saskatchewan'), ('NL', 'Terre-Neuve-et-Labrador'), ('NT', 'Territoires du Nord-Ouest'), ('YT', 'Yukon'), ('PE', 'Île-du-Prince-Édouard')])),
            ],
        ),
    ]
