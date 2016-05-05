from django.conf.urls import url, include
from .views import CmsView



def create_urls(pages):
    out = []
    for page_name in pages:
        
        page = pages[page_name]
        extra_modules = page.get('extra_modules', [])
        comp_url = r'^%s$' % page['url']
        u = url(comp_url, CmsView.as_view(
                page_name=page_name, extra_modules=extra_modules
            ), name=page_name
        )
        out.append(u)

    return out

    