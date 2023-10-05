from user_page import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']
def create(self, validated_data):
        user = MyUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user