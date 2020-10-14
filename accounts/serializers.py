from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


from django.contrib.auth import authenticate
from rest_framework import exceptions



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_date):
        user = User.objects.create_user(validated_date['username'], validated_date['email'], validated_date['password'])
        return user
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class UserLogin(serializers.ModelSerializer):
    username=serializers.CharField(max_length=32, required=True)
    password=serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username','password')

    def validate(self,data):
        username=data.get('username')
        password=data.get('password')
        if username and password:
            auth=authenticate(username=username, password=password)
            if auth:
                return auth
            else:
                raise exceptions.ValidationError('Username or Password Invalid')
        else:
            raise exceptions.ValidationError('fill all the fields')




# class UserLogin(serializers.ModelSerializer):
#     username=serializers.CharField(max_length=32, required=True)
#     password=serializers.CharField(min_length=8, write_only=True)

#     class Meta:
#         model = User
#         fields = ('username','password')

#     def validate(self,data):
#         username=data.get('username')
#         password=data.get('password')
#         if username and password:
#             auth=authenticate(username=username, password=password)
#             if auth:
#                 return auth
#             else:
#                 raise  exceptions.ValidationError('Username or Password Invalid')
#         else:
#             raise exceptions.ValidationError('fill all the fields')