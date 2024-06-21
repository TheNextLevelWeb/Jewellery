from .models import NearByStores
from rest_framework import serializers

class NBSSerializer(serializers.ModelSerializer):

    class Meta:
        model = NearByStores
        fields = '__all__'