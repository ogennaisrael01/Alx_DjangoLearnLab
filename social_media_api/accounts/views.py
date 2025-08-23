from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from accounts.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationApiView(generics.CreateAPIView):
    permission_classes = []
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)  
            return Response({"Token":token.key})
        else:
            return Response({"Detail": "Invalid Credentials"})

class LoginApiView(APIView):
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            
            user = authenticate(request, email=email, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"Token": token.key})
            else:
                return Response({"Detail": "User not found"})
        return Response({"Detail": "Invalid Credentials"})