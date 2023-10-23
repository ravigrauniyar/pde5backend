from rest_framework import serializers


class EventListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    source_name = serializers.CharField(source='source.name')
    properties = serializers.JSONField()


class EventCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    source_id = serializers.IntegerField()
    properties = serializers.JSONField()


class EventDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    source_name = serializers.CharField(source='source.name')
    properties = serializers.JSONField()
