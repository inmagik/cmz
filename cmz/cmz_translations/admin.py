from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import TranslatedText

admin.site.register(TranslatedText, TranslatableAdmin)
