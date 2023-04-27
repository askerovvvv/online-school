from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import RegisterSerializer, ForgotPasswordSerializer, CreateNewPasswordSerializer

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = "You have successfully registered. An activation email has been sent to you."
            return Response(message, status=201)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivateUserApiView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return HttpResponse("Your account have been successfully activated!")
        except User.DoesnotExist:
            return HttpResponse('Your activation code is not valid please check it again and try')


class ForgotPasswordApiView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_code()
            return HttpResponse('An activation code has been sent to change your password!', status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


class CreateNewPasswordApiView(APIView):
    def post(self, request):
        serializer = CreateNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.change_password()
            return  HttpResponse('Your password has been successfully changed!', status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
