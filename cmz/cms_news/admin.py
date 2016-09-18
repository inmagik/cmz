from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import News

admin.site.register(News, TranslatableAdmin)
