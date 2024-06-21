from rest_framework import serializers
from .models  import Support

class SupporSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = Support
        fields = '__all__'
