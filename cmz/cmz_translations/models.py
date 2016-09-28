from __future__ import unicode_literals

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from hvad.utils import get_translation_aware_manager


class TranslatedText(TranslatableModel):

    context = models.CharField(max_length=200, null=True, blank=True)
    label = models.CharField(max_length=200)
    translations = TranslatedFields(
        body = models.TextField()
    )

    def __unicode__(self):
        if not self.context:
            return self.label
        return '%s [%s]' % (self.label, self.context)
