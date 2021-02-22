from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from rest_framework.authtoken import views

from config.api import api

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("logout/", logout, {"next_page": "/"}, name="logout"),
    path("api/", include(api.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", views.obtain_auth_token),
]

urlpatterns.append(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)[0])
urlpatterns.append(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)[0])
