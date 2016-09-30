from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
import json

register = template.Library()
COOKIECONSENT_OPTIONS = getattr(settings, "COOKIECONSENT_OPTIONS", {})
if type(COOKIECONSENT_OPTIONS) != dict:
    raise TypeError("COOKIECONSENT_OPTIONS must be a dict")

if 'link' in COOKIECONSENT_OPTIONS and not COOKIECONSENT_OPTIONS['link'].startswith("/"):
    try:
        COOKIECONSENT_OPTIONS['link'] = reverse(COOKIECONSENT_OPTIONS['link'])
        print COOKIECONSENT_OPTIONS['link']
    except NoReverseMatch:
        pass

#TODO: max_len is useless here, should be moved to model somehow
@register.inclusion_tag('cms_cookieconsent/cookieconsent_script.html')
def cookieconsent_script():
    return {
        "COOKIECONSENT_OPTIONS" : json.dumps(COOKIECONSENT_OPTIONS),
    }
