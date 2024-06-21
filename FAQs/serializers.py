from rest_framework import serializers
from .models import FAQs, PrivacyPolicy

class FAQsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQs
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'