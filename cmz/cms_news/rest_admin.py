from django_rest_admin.register import rest_admin, RestAdminConfig
from .models import News
from hvad.contrib.restframework import TranslatableModelSerializer


#TODO: this is needed because rest_framework.filters.OrderingFilter breaks django-hvad
from rest_framework.viewsets import ModelViewSet
from django.utils import translation
class NewsViewSet(ModelViewSet):
    def get_queryset(self):
        return News.objects.language(translation.get_language()).all()

class NewsConfig(RestAdminConfig):
    serializer_class = TranslatableModelSerializer
    viewset_class = NewsViewSet

rest_admin.register(News, NewsConfig)
