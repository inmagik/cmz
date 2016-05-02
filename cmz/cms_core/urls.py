from django.conf.urls import url, include
from .urls_helpers import create_urls
from django.conf import settings

urlpatterns = []



SITE_PAGES = getattr(settings, 'SITE_PAGES')

urlpatterns += create_urls(SITE_PAGES)