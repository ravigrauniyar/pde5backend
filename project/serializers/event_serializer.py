from rest_framework import serializers
from project.models.source import Source

class EventListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class EventCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    properties = serializers.JSONField(required=False)

class EventDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    source_name = serializers.CharField(source='source.name')
    properties = serializers.JSONField()