from __future__ import unicode_literals

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from hvad.utils import get_translation_aware_manager

class News(TranslatableModel):

    date = models.DateField(auto_now_add=True)
    translations = TranslatedFields(
        title = models.CharField(max_length=300),
        body = models.TextField()
    )
