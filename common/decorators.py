from django.http import HttpResponseBadRequest
from django.shortcuts import HttpResponse


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def ajax_required(f):

    def wrap(request, *args, **kwargs):
        if not is_ajax(request):
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
