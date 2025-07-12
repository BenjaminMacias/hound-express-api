from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Guia, Estatus, Usuario
from .serializers import GuiaSerializer, EstatusSerializer, UsuarioSerializer

class GuiaViewSet(viewsets.ModelViewSet):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer

    def update(self, request, *args, **kwargs):
        guia = self.get_object()
        old_status = guia.currentStatus
        response = super().update(request, *args, **kwargs)
        guia.refresh_from_db()
        new_status = guia.currentStatus
        if old_status != new_status:
            Estatus.objects.create(
                guia=guia,
                status=new_status,
                updatedBy=request.user.username if request.user.is_authenticated else "anon"
            )
        return response

    @action(detail=False, methods=["post"], url_path="crear-guia")
    def crear_guia(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            guia = serializer.save()
            return Response(self.get_serializer(guia).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["put"], url_path="actualizar-guia")
    def actualizar_guia(self, request, pk=None):
        guia = self.get_object()
        old_status = guia.currentStatus
        serializer = self.get_serializer(guia, data=request.data, partial=True)
        if serializer.is_valid():
            guia = serializer.save()

            # Forzar actualización de la fecha
            guia.updatedAt = timezone.now()
            guia.save()

            # Si cambió el estado, registrar historial
            new_status = guia.currentStatus
            if old_status != new_status:
                Estatus.objects.create(
                    guia=guia,
                    status=new_status,
                    updatedBy=request.user.username if request.user.is_authenticated else "anon"
                )

            return Response(self.get_serializer(guia).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"], url_path="obtener-guia")
    def obtener_guia(self, request, pk=None):
        guia = self.get_object()
        serializer = self.get_serializer(guia)
        return Response(serializer.data)

    @action(detail=True, methods=["delete"], url_path="eliminar-guia")
    def eliminar_guia(self, request, pk=None):
        guia = self.get_object()
        guia.delete()
        return Response({"mensaje": "Guía eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

class EstatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estatus.objects.all()
    serializer_class = EstatusSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
