from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Q
from rest_framework import serializers

from account.mass_email import mass_email_send
from account.models import MassEmails
from account.send_code import send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)

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


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Account not found!')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_mail(
            "This is you new activation code to change your password. Please save it and do not lose ",
            user.activation_code,
            'bekbol.2019@gmail.com',
            [email]
        )


class CreateNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True) #Todo: required true is it
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True, min_length=6)
    activation_code = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        activation_code = attrs.get('activation_code')

        if password != password2:
            raise serializers.ValidationError('Password do not match')

        if not User.objects.filter(activation_code=activation_code, email=email).exists():
            raise serializers.ValidationError("Check your activation code or email!")

        return attrs

    def change_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()


class MassEmailSerializer(serializers.ModelSerializer):
    # subject =  #todo: auto

    class Meta:
        model = MassEmails
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data.get("to"))
        users = validated_data.get("to")
        subj = validated_data.get("subject")
        bod = validated_data.get("body")

        mass_mail_data = MassEmails.objects.create(subject=subj, body=bod)
        mass_mail_data.to.set(users)
        print(mass_mail_data.to)
        # users2 = User.objects.filter(Q(email__icontains=mass_mail_data.to))
        # print(User.objects.all().email)
        mass_email_send(subj, bod, User.objects.all())
        return mass_mail_data