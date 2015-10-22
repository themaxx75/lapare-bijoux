# -*- coding: utf-8 -*-

import glob

from django.shortcuts import render_to_response
from django.template import RequestContext
from settings import STATICFILES_DIRS
from www.models import Vente, Expo


def site_root(request):
    context_dict = {}
    context = RequestContext(request)
    context_dict['carousel'] = [x.split('/')[-1:][0] for x in glob.glob(
        STATICFILES_DIRS[0] + '/img/carousel/*.jpeg')]

    context_dict['ventes_quebec'] = Vente.objects.filter(province=8)
    context_dict['ventes_autres'] = Vente.objects.all().exclude(province=8)
    context_dict['expo'] = Expo.objects.all().order_by('start')

    return render_to_response('index.html', context_dict, context)
