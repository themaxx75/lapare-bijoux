import glob

from django.shortcuts import render_to_response
from django.template import RequestContext
from lapare.settings import MEDIA_ROOT, MEDIA_URL


def site_root(request):
    context_dict = {}
    context = RequestContext(request)
    context_dict['carousel'] = [x.split('/')[-1:][0] for x in glob.glob(
        MEDIA_ROOT + '/*.jpg')]
    print(context_dict['carousel'])
    return render_to_response('index.html', context_dict, context)
