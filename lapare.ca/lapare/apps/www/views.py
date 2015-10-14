from django.shortcuts import render_to_response
from django.template import RequestContext


def site_root(request):
    context_dict = {}
    context = RequestContext(request)
    return render_to_response('index.html', context_dict, context)
