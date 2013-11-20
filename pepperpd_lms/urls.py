from django.conf.urls import url

from lms.urls import urlpatterns

_default = object()


def override(regex, view, name=None):
    for i, p in enumerate(urlpatterns):
        if getattr(p, 'name', _default) == name or p.regex.pattern == regex:
            urlpatterns[i] = url(regex, view, name)


# This is how you would override a particular view callable already defined
# in edX.
override(r'^update_certificate', 'poc.view')

# Of course, you can add new views:
urlpatterns += [
    url(r'^helloworld$', 'poc.view'),
]
