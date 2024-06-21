from rest_framework import serializers
from users.models import Users

class UserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    saved_address = serializers.CharField(required=False)
    order_history = serializers.JSONField(required=False)
    wish_list = serializers.JSONField(required=False)
    feedback = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = '__all__'

    def validate_email(self, value):
        if Users.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists.")
        return value

    def validate_username(self, value):
        if Users.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "A user with this username already exists.")
        return value


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = Users
        fields = ['username', 'password']

    

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError(
                "Both username and password are required.")

        return data


class ChangePasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    class Meta:
        model = Users
        fields = '__all__'


class ForgotPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    new_password = serializers.CharField()

    class Meta:
        model = Users
        fields = '__all__'

class SOWSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [ 'saved_address', 'wish_list', 'order_history']