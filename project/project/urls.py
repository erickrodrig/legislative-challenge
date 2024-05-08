from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("project.portal.urls", "portal"), namespace="portal")),
    path("api/", include("project.api.urls")),
    path("auth/", include(("project.authentication.urls", "authentication"), namespace="auth")),
]
