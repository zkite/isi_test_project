from rest_framework import serializers

from dialogs.models import Thread, Message
from dialogs.validators import admin_validator


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = "__all__"
        validators = [admin_validator]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
