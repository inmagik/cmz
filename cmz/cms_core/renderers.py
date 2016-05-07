from django_medusa.renderers import StaticSiteRenderer
from django.conf import settings
from .urls_helpers import create_urls
SITE_PAGES = getattr(settings, 'SITE_PAGES')

urls = [ u._regex for u in create_urls(SITE_PAGES) ]
print urls

class CMSRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/"
        ])

renderers = [CMSRenderer, ]