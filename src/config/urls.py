from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("up/", include("up.urls")),
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
    path("api/shipments/", include("shipments.urls")),  # tu API de shipments, siempre disponible
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        *urlpatterns,
    ]
