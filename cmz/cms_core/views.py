from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.

class CmsView(TemplateView):
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


    def get_template_names(self):
        if self.template:
            return [ self.template ]
        return [ "%s.html" % self.page_name, ]
