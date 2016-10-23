#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import template
from ..models import TextContent

register = template.Library()

#TODO: max_len is useless here, should be moved to model somehow
@register.inclusion_tag('cms_content/cms_text_content.html')
def cms_text_content(key, max_len=None):
    try:
        content = TextContent.objects.get(key=key)
        return {'content': content, 'key': key}

    except TextContent.DoesNotExist:
        return { 'content': None, 'key': key }
