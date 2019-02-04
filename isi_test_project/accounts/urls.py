from django.urls import path
from accounts.views import UserListAPIView


urlpatterns = [
    path('jwt-token/', UserListAPIView.as_view(), name='jwt-token'),
]