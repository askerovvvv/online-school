from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from teacher.models import TeacherInformation
from teacher.serializers import TeacherInfoSerializer


class TeacherInfoApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeacherInformation.objects.all()
    serializer_class = TeacherInfoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetTeacherInfoApiView(ListAPIView):
    queryset = TeacherInformation.objects.all()
    serializer_class = TeacherInfoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(teacher=True)
        return queryset



