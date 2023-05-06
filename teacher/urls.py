from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course.views import *
from teacher.views import TeacherInfoApiView

# router = DefaultRouter()
# router.register('', TeacherInfoApiView, basename='teacher')


urlpatterns = [
    path('', TeacherInfoApiView.as_view(), name='teacher'),
]