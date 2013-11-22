from django.conf.urls import url
from lms.urls import urlpatterns
from pepperpd.utils import override_patterns

override = override_patterns(urlpatterns)


# This is how you would override a particular view callable already defined
# in edX.
override(r'^update_certificate$', 'poc.view')

# Of course, you can add new views:
urlpatterns += [
    url(r'^helloworld$', 'poc.view'),
]
