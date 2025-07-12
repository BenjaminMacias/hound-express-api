from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuiaViewSet, EstatusViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'guias', GuiaViewSet, basename='guias')
router.register(r'estatuses', EstatusViewSet, basename='estatuses')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]
