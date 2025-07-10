from rest_framework import serializers
from .models import Guide, StatusChange

class StatusChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusChange
        fields = ['id', 'previous', 'new', 'timestamp']

class GuideSerializer(serializers.ModelSerializer):
    history = StatusChangeSerializer(many=True, read_only=True)

    class Meta:
        model = Guide
        fields = ['id', 'number', 'status', 'created_at', 'history']
