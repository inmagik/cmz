#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import template
from django.utils.safestring import mark_safe

register = template.Library()
from ..settings import get_seo_value, SEO_ENCODING

def load_seo_value(tag, page):
    value =  get_seo_value(tag, page)
    return value.decode(SEO_ENCODING)


@register.simple_tag(takes_context=True)
def seo_tag(context, tag, target_attr="name"):
    value = load_seo_value(tag, context["view"].page_name)
    html = '<meta %s="%s" content="%s" />' % (target_attr, tag, value)
    return mark_safe(html)

@register.simple_tag(takes_context=True)
def seo_value(context, tag):
    value = load_seo_value(tag, context["view"].page_name)
    return mark_safe(value)
