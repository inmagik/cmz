from __future__ import unicode_literals

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from hvad.utils import get_translation_aware_manager
from django.conf import settings

SITE_PAGES = getattr(settings, 'SITE_PAGES', {})
SITE_PAGES_CHOICES = [(x, x) for x in sorted(SITE_PAGES.keys())]

class SEOOverride(TranslatableModel):

    page = models.CharField(max_length=255, choices=SITE_PAGES_CHOICES, null=True, blank=True)
    tag = models.CharField(max_length=255)
    translations = TranslatedFields(
        content = models.TextField(null=True, blank=True)
    )

    def __unicode__(self):
        return '%s - %s' % (self.page, self.tag)

    class Meta:
        ordering = ["page", "tag"]
