from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import SEOOverride

admin.site.register(SEOOverride, TranslatableAdmin)
