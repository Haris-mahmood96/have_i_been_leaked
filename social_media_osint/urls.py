from django.contrib import admin
from django.urls import path, include
from social_media_osint_api import urls as social_media_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(social_media_urls)),
]
