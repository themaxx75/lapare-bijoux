from django.db import models


class Expo(models.Model):
    start = models.DateField()
    end = models.DateField()
    adresse = models.TextField()
    description = models.TextField()


class Vente(models.Model):
    nom = models.TextField()
    PROVINCES = (
        (1, 'Alberta'),
        (2, 'Colombie-Britannique'),
        (3, 'Manitoba'),
        (4, 'Nouveau-Brunswick'),
        (5, 'Nouvelle-Écosse'),
        (6, 'Nunavut'),
        (7, 'Ontario'),
        (8, 'Québec'),
        (9, 'Saskatchewan'),
        (10, 'Terre-Neuve-et-Labrador'),
        (11, 'Territoires du Nord-Ouest'),
        (12, 'Yukon'),
        (13, 'Île-du-Prince-Édouard'),
    )
    province = models.IntegerField(choices=PROVINCES)
    adresse = models.TextField()
    url = models.URLField(default=None, blank=True)


class Bijoux(models.Model):
    image = models.ImageField()
