"""cmz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from solid_i18n.urls import solid_i18n_patterns


patterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('django_rest_admin.urls')),
    url(r'', include('cms_core.urls')),
]

try:
    # Importing modules declared for current website
    import website.urls
    patterns += [
        url(r'', include('website.urls'))
    ]
except:
    raise


urlpatterns = solid_i18n_patterns('', *patterns)



from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
