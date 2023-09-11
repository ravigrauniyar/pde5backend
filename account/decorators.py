# decorators.py
from django.conf import settings
from django.http import HttpResponseForbidden

def debug_only(view_func):
    def wrapper(request, *args, **kwargs):
        if settings.DEBUG:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("This view is disabled in production.")
    return wrapper
