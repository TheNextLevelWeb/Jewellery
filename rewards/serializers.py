from rest_framework import serializers
from .models import Rewards


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = '__all__'
