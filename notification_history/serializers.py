from rest_framework import serializers
from .models import Notification_history


class NHSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification_history
        fields = '__all__'
