from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    def create(self, validated_data): 
        user = User.objects.create_user(
            username = validated_data['username'], 
            email = validated_data['email'],
            password = validated_data['password'], 
            name = validated_data['name'],
            role = validated_data['role'],
            allow_noti = validated_data['allow_noti']
        )
        return user 
    class Meta: 
        model = User
        fields = ['username', 'email', 'name', 'password', 'role', 'allow_noti'] # 직렬화 