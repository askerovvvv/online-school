from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import RegisterSerializer


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
            return HttpResponse('Your activation code is not valid\n please check it again and try')

