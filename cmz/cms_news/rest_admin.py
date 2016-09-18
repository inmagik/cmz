from django_rest_admin.register import rest_admin, RestAdminConfig
from .models import News
from hvad.contrib.restframework import TranslatableModelSerializer

class NewsConfig(RestAdminConfig):
    serializer_class = TranslatableModelSerializer

rest_admin.register(News, NewsConfig)
