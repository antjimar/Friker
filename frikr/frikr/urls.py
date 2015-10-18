from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from pho import urls as photos_web_urls
from photos import api_urls as photos_api_urls
#from photos impor api_1_1_urls as photos_api_1_1_urls      para la version 1.1 de nuestro api

admin.autodiscover()


urlpatterns = patterns('',

    # Admin URLS
    url(r'^admin/', include(admin.site.urls)),

    # Web URLS
    url(r'', include(photos_web_urls)),

    # API 1.0 URLS
    url(r'^api/1.0/', include(photos_api_urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
