from rest_framework import serializers
from shop.serializers import ProductSerializer
from .models import Cart

class CartSerializers(serializers.ModelSerializer):
    
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['id','quantity','product']

class AddToCartSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = '__all__'
    
