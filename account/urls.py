from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivateUserApiView.as_view()),
]


