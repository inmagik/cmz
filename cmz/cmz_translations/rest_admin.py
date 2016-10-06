from django_rest_admin.register import rest_admin, RestAdminConfig
from .models import TranslatedText
from hvad.contrib.restframework import TranslatableModelSerializer


#TODO: this is needed because rest_framework.filters.OrderingFilter breaks django-hvad
from rest_framework.viewsets import ModelViewSet
from django.utils import translation
class TranslatedTextViewSet(ModelViewSet):
    def get_queryset(self):
        return TranslatedText.objects.language(translation.get_language()).all()

class TranslatedTextConfig(RestAdminConfig):
    serializer_class = TranslatableModelSerializer
    viewset_class = TranslatedTextViewSet

rest_admin.register(TranslatedText, TranslatedTextConfig)
