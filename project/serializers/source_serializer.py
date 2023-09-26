from rest_framework import serializers

class SourceCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False)

class SourceListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    tag = serializers.CharField()
    source_key = serializers.CharField(read_only=True)
    source_secret = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class SourceDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    tag = serializers.CharField()
    source_key = serializers.CharField(read_only=True)
    source_secret = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class SourceUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
