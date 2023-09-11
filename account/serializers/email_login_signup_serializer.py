from account.models import UserAccount
from rest_framework import serializers

class EmailSignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    avatar = serializers.ImageField(required=False)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data['username'] = validated_data['email']
        user = UserAccount(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

class EmailSignInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()