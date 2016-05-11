from django import template
from django.conf import settings
import json

register = template.Library()
COOKIECONSENT_OPTIONS = getattr(settings, "COOKIECONSENT_OPTIONS", {})
if type(COOKIECONSENT_OPTIONS) != dict:
    raise TypeError("COOKIECONSENT_OPTIONS must be a dict")

#TODO: max_len is useless here, should be moved to model somehow
@register.inclusion_tag('cms_cookieconsent/cookieconsent_script.html')
def cookieconsent_script():
    return {
        "COOKIECONSENT_OPTIONS" : json.dumps(COOKIECONSENT_OPTIONS),
    }