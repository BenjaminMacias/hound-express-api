from rest_framework import viewsets
from .models import Guide, StatusChange
from .serializers import GuideSerializer, StatusChangeSerializer

class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def update(self, request, *args, **kwargs):
        guide = self.get_object()
        old_status = guide.status
        response = super().update(request, *args, **kwargs)
        guide.refresh_from_db()
        new_status = guide.status
        if old_status != new_status:
            StatusChange.objects.create(
                guide=guide,
                previous=old_status,
                new=new_status
            )
        return response

class StatusChangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StatusChange.objects.all()
    serializer_class = StatusChangeSerializer
