from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course.views import *

router = DefaultRouter()
router.register('', CourseModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]