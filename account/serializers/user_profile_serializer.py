from rest_framework import serializers


class UserDetailSerailizer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()