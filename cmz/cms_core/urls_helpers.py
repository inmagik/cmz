from django.conf.urls import url, include
from .views import CmsView



def create_urls(pages):
    out = []
    empty_urls = []
    for page_name in pages:

        page = pages[page_name]
        extra_modules = page.get('extra_modules', [])
        if page['url']:
            comp_url = r'^%s/$' % page['url']
        else:
            comp_url = r'^$'

        u = url(comp_url, CmsView.as_view(
                page_name=page_name, extra_modules=extra_modules
            ), name=page_name
        )

        if page['url']:
            out.append(u)
        else:
            empty_urls.append(u)

        if len(empty_urls) > 2:
            raise ValueError("CMZ ERROR: your pages.py has more than one empty url")


    #trick for allowing ''
    out.extend(empty_urls)

    return out
