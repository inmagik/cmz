from django import template
from ..models import TranslatedText
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def cmz_translation(context, label, page_context=None):
    page = context['request'].GET.get('page', 1);
    page = int(page)
    try:
        instance = TranslatedText.objects.language().get(label=label, context=page_context)
        return mark_safe(instance.body)
    except TranslatedText.DoesNotExist:
        return "Not translated"
