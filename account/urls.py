from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('activate/<uuid:activation_code>/', ActivateUserApiView.as_view()),
    path('forgot-password/', ForgotPasswordApiView.as_view()),
    path('create-new-password/', CreateNewPasswordApiView.as_view()),
]


