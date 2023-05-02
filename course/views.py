from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from course.models import Course
from course.serializers import CourseSerializers


class CourseModelViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]