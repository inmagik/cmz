from __future__ import unicode_literals

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

class News(TranslatableModel):
    
    translations = TranslatedFields(
        text = models.TextField()
    )
