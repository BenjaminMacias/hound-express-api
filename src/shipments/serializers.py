from rest_framework import serializers
from .models import Guia, Estatus, Usuario
from django.utils import timezone


class GuiaSerializer(serializers.ModelSerializer):
    trackingNumber = serializers.CharField()
    origin = serializers.CharField()
    destination = serializers.CharField()
    recipient = serializers.CharField(default="", allow_blank=True)
    creationDate = serializers.DateTimeField(source="createdAt", required=False)
    lastUpdate = serializers.DateTimeField(source="updatedAt", read_only=True)
    status = serializers.CharField(source="currentStatus")
    history = serializers.SerializerMethodField()  # boton modal

    class Meta:
        model = Guia
        fields = [
            "id",
            "trackingNumber",
            "origin",
            "destination",
            "recipient",
            "creationDate",  # input/output
            "lastUpdate",    # solo output
            "status",         # input/output
            "history",  #  boton modal
        ]

    def create(self, validated_data):
        validated_data["createdAt"] = validated_data.get("createdAt", timezone.now())
        validated_data["updatedAt"] = timezone.now()
        return Guia.objects.create(**validated_data)

    def get_history(self, obj):
        estatuses = obj.estatuses.all().order_by("timestamp")
        return [
            {
                "date": e.timestamp.isoformat(),
                "status": e.status,
                "location": "Ubicación no disponible",  # Si no hay un campo real
                "notes": f"Actualizado por {e.updatedBy}",
            }
            for e in estatuses
        ]

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == "currentStatus":
                setattr(instance, "currentStatus", value)
            elif attr == "createdAt":
                setattr(instance, "createdAt", value)
            elif attr != "updatedAt":
                setattr(instance, attr, value)
        instance.updatedAt = timezone.now()
        instance.save()
        return instance


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatus
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
