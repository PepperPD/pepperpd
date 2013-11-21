from django.conf.urls import url
from cms.urls import urlpatterns
from pepperpd.utils import override_patterns

override = override_patterns(urlpatterns)


# This is how you would override a particular view callable already defined
# in edX.
override(r'^howitworks$', 'poc.view')

# Of course, you can add new views:
urlpatterns += [
    url(r'^helloworld$', 'poc.view'),
]
