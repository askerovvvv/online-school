from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True, required=True) #Todo: write_only what is it
    class Meta:
        model = User
        fields = ("email", "password", "password2")

    def validate(self, attrs):
        password2 = attrs.get('password2')
        password = attrs.get('password')

        if password != password2:
            raise serializers.ValidationError('Password do not match')
        return attrs


