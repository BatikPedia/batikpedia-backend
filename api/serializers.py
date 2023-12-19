from .models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        )
    


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user