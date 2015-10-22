# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from PIL import Image
import glob
from lapare.settings import MEDIA_ROOT, STATICFILES_DIRS
import hashlib
from django.core.management import call_command
import os


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        resize_gallery()


def resize_gallery(max_height=800):
    files = [x for x in glob.glob(MEDIA_ROOT + '/*.jpg')]
    old_files = [x for x in STATICFILES_DIRS[0] + '/img/carousel/*']
    for f in old_files:
        os.remove(f)

    for file in files:
        with open(file, 'rb') as f:
            name = '{path}/img/carousel/{name}.jpeg'.format(
                path=STATICFILES_DIRS[0],
                name=hashlib.md5(f.read()).hexdigest()
            )

        img = Image.open(file)
        height_percent = (max_height/float(img.height))
        width_size = int((float(img.width)*float(height_percent)))
        img = img.resize((width_size, max_height), Image.ANTIALIAS)
        img.save(name, 'JPEG', quality=90)
        print(name)

    call_command('collectstatic', verbosity=0, interactive=False)
