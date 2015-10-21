import glob

from django.shortcuts import render_to_response
from django.template import RequestContext
from settings import MEDIA_ROOT, STATICFILES_DIRS


def site_root(request):
    context_dict = {}
    context = RequestContext(request)
    context_dict['carousel'] = [x.split('/')[-1:][0] for x in glob.glob(
        STATICFILES_DIRS[0] + '/img/carousel/*.jpeg')]
    print(STATICFILES_DIRS[0] + '/img/carousel/*.jpeg')
    print(context_dict['carousel'])
    return render_to_response('index.html', context_dict, context)
