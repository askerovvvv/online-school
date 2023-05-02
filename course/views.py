from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from course.models import *
from course.serializers import CourseSerializer, SavedSerializer


class CourseModelViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    @action(methods=['POST'], detail=True)
    def saved(self, request, pk):
        course = self.get_object()    # Todo:ask what is ...
        saved_obj, _ = Saved.objects.get_or_create(course=course, user=request.user)
        saved_obj.saved = not saved_obj.saved
        saved_obj.save()
        status = 'Added to saved'
        if not saved_obj.saved:
            status = 'Removed from saved'
        return Response({'status': status})


class SavedCourseList(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(user=user, saved=True)
        return queryset

