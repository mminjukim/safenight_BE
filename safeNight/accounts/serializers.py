from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    def create(self, validated_data): 
        user = User.objects.create_user(
            username = validated_data['username'], 
            email = validated_data['email'], # 회원가입시 이메일 입력 받음 
            last_name = validated_data['last_name'],
            password = validated_data['password'],  
        )
        user.groups.set(validated_data['groups']) # 사용자에 그룹 설정 
        return user 
    class Meta: 
        model = User
        fields = ['username', 'email', 'last_name', 'password', 'groups'] # 직렬화 