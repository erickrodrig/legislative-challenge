from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("project.portal.urls")),
    path("api/", include("project.api.urls")),
]
