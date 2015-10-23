# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from www.models import Bijoux, Expo, Vente


def site_root(request):
    context_dict = {}
    context = RequestContext(request)
    context_dict['carousel'] = [b.processed for b in Bijoux.objects.all()]

    context_dict['ventes_quebec'] = Vente.objects.filter(province=8)
    context_dict['expo'] = Expo.objects.all().order_by('start')
    ventes_autres = {}

    for province in Vente.PROVINCES:
        if province[0] == 8:
            continue

        results = Vente.objects.filter(province=province[0])

        if results:
            ventes_autres[province[1]] = results

    context_dict['ventes_autres'] = ventes_autres

    return render_to_response('index.html', context_dict, context)
