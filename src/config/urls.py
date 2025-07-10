from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Rutas estándar con DRF router (esto sigue funcionando)
    path("api/shipments/", include("shipments.urls")),

    # Rutas adicionales para práctica 3 (usando alias más amigables)
    path("api/crear-guia/", include("shipments.urls")),        # POST
    path("api/actualizar-guia/", include("shipments.urls")),   # PUT (requiere ID en URL)
    path("api/obtener-guia/", include("shipments.urls")),      # GET (requiere ID)
    path("api/eliminar-guia/", include("shipments.urls")),     # DELETE (requiere ID)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        *urlpatterns,
    ]


