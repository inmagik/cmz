from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.utils import translation


class CMZTemplateMixin(object):
    def get_template_names(self):
        if self.template:
            name = self.template
        else:
            name = "%s.html" % self.page_name

        lang = translation.get_language()
        if name.endswith(".html"):
            translated_name = name.replace(".html", ".%s.html" % lang)
        else:
            translated_name = name + ".%s" % lang

        return [ translated_name, name ]


class CmsView(CMZTemplateMixin, TemplateView):
    """
    Serving frontend pages
    """

    page_name = None
    template = None
    extra_modules = []

    def __init__(self, *args, **kwargs):
        self.extra_modules = kwargs.pop('extra_modules', [])
        self.page_name = kwargs.pop('page_name')
        if 'template' in kwargs:
            self.template = kwargs.pop('template')
        else:
            self.template = None
        super(CmsView, self).__init__(*args, **kwargs)


    def get_context_data(self, **kwargs):
        ctx = super(CmsView, self).get_context_data(**kwargs)
        ctx['view_kwargs'] = self.kwargs
        return ctx
