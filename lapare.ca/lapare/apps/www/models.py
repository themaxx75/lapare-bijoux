import hashlib
import os

from django.core.management import call_command
from django.db import models
from lapare.settings import STATIC_URL, STATICFILES_DIRS
from PIL import Image


class Expo(models.Model):
    start = models.DateField()
    end = models.DateField()
    adresse = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.description


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

    def __str__(self):
        return self.nom


# To process bulk delete in Admin
class BijouxQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in self:
            try:
                os.remove(obj.image.path)
            except FileNotFoundError:
                pass

            try:
                os.remove(obj.processed_path)
            except FileNotFoundError:
                pass

        super(BijouxQuerySet, self).delete(*args, **kwargs)


class Bijoux(models.Model):
    objects = BijouxQuerySet.as_manager()
    image = models.ImageField()
    processed = models.TextField(default=None, blank=True)
    processed_path = models.TextField(default=None, blank=True)

    def image_tag(self):
        if self.processed:
            return '<img src="{url}" width="50%" height="50%" />'.format(
                url=STATIC_URL + 'img/carousel/' + self.processed
            )
        else:
            return ''
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    @property
    def max_height(self):
        return 800

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        name = '{name}.jpeg'.format(
            path=STATICFILES_DIRS[0],
            name=hashlib.md5(self.image.file.read()).hexdigest()
        )
        self.image.file.seek(0)
        self.processed = name

        img = Image.open(self.image.file)
        height_percent = (self.max_height/float(img.height))
        width_size = int((float(img.width)*float(height_percent)))
        img = img.resize((width_size, self.max_height), Image.ANTIALIAS)
        self.processed_path = '{path}/img/carousel/{name}'.format(
            path=STATICFILES_DIRS[0],
            name=self.processed
        )
        img.save(self.processed_path, 'JPEG', quality=90)
        call_command('collectstatic', verbosity=0, interactive=False)

        super(Bijoux, self).save(force_insert, force_update)

    def delete(self, *args, **kwargs):
        try:
            # Removing uploaded file
            os.remove(self.image.path)
        except FileNotFoundError:
            pass

        try:
            # Removing processed file
            os.remove(self.processed_path)
        except FileNotFoundError:
            pass

        super(Bijoux, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.image)
