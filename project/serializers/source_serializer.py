from rest_framework import serializers

class SourceListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    tag = serializers.CharField()
    project_id = serializers.IntegerField()

class SourceDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    tag = serializers.CharField()
    project_id = serializers.IntegerField()
    key = serializers.CharField(read_only=True)
    secret = serializers.CharField(read_only=True)
