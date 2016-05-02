from django import template
from ..models import News

register = template.Library()

@register.simple_tag(takes_context=True)
def cms_news_list(context, num_items=10):
    page = context['request'].GET.get('page', 1);
    page = int(page)
    #todo: add num pages, total items..
    return News.objects.all()[(page-1)*num_items:num_items]

    