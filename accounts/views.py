from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer, UserLogin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request, format='json'):
        serializer = UserLogin(data=request.data)
        serializer.is_valid(raise_exception=True)
        objectuser = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=objectuser)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)




# class LoginView(APIView):
#     def post(self, request, format='json'):
#         serializer = UserLogin(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         objectuser = serializer.validated_data
#         token, _ = Token.objects.get_or_create(user=objectuser)
#         return Response(token.key, headers={"Access-Control-Allow-Origin": "*"})