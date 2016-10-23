#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import translation

from .models import SEOOverride

CMZ_SEO = getattr(settings, "CMZ_SEO", {})
CMZ_SEO_LANGS = getattr(settings, "CMZ_SEO_LANGS", {})
SEO_ENCODING = getattr(settings, "CMZ_SEO_ENCODING", 'utf-8')

def get_seo_value(tag, page=None, lang=True):
    if lang:
        current_lang = translation.get_language()

        try:
            obj = SEOOverride.objects.language().get(tag=tag, page=page)
            value = obj.content or ""

        except SEOOverride.DoesNotExist:
            if current_lang in  CMZ_SEO_LANGS:
                value = CMZ_SEO_LANGS[current_lang].get(tag, CMZ_SEO.get(tag, ""))
            else:
                value = CMZ_SEO.get(tag, "")
        return value

    return CMZ_SEO.get(tag, "")
