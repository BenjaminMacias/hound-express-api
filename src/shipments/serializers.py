from rest_framework import serializers
from .models import Guia, Estatus, Usuario

class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatus
        fields = ['id', 'status', 'timestamp', 'updatedBy']

class GuiaSerializer(serializers.ModelSerializer):
    estatuses = EstatusSerializer(many=True, read_only=True)

    class Meta:
        model = Guia
        fields = [
            'id',
            'trackingNumber',
            'origin',
            'destination',
            'createdAt',
            'updatedAt',
            'currentStatus',
            'estatuses',
        ]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id',
            'name',
            'email',
            'password',
            'createdAt',
            'updatedAt',
        ]
