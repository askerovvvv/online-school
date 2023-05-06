from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from teacher.models import TeacherInformation
from teacher.serializers import TeacherInfoSerializer


class TeacherInfoApiView(CreateAPIView):
    queryset = TeacherInformation.objects.all()
    serializer_class = TeacherInfoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


