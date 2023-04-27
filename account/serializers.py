from django.contrib.auth import get_user_model
from rest_framework import serializers

from account.send_code import send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True) #Todo: write_only what is it

    class Meta:
        model = User
        fields = ("email", "password", "password2")

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        password = attrs.get('password')

        if password != password2:
            raise serializers.ValidationError('Password do not match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_activation_code(user.email, code)
        return user

