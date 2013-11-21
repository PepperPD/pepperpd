from django.conf.urls import url


def override_patterns(urlpatterns):
    def override(regex, view, name=None):
        for i, p in enumerate(urlpatterns):
            p_name = getattr(p, 'name', None)
            if (p_name and p_name == name) or p.regex.pattern == regex:
                urlpatterns[i] = url(regex, view, name)
                break
        else:
            raise ValueError(
                "Could not find pattern: regex=%s, name=%s" % (regex, name))

    return override
