from rest_framework import viewsets
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

class EstatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estatus.objects.all()
    serializer_class = EstatusSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
