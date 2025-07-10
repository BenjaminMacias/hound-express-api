from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GuiaViewSet, EstatusViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'guias', GuiaViewSet, basename='guia')
router.register(r'estatus', EstatusViewSet, basename='estatus')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
]
