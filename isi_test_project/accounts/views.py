from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView


class UserListAPIView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer
