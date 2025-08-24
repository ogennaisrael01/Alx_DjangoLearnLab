from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from accounts.serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from accounts.permissions import IsOwner

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
    

class UserApiView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        ...
    def partial_update(self, request, *args, **kwargs):
        ...
    def retrieve(self, request, *args, **kwargs):
        ...
    def destroy(self, request, *args, **kwargs):
        ...
    
    def get_permissions(self):
        
        if self.action == "update" or "delete" or "partial_update":
            permission_classes = [permissions.IsAuthenticated(), IsOwner()]
        else:
            permission_classes = [permissions.IsAuthenticated()]
        return permission_classes

        
    @action(methods=["post"], url_path="follow_user", detail=True)
    def follow_user(self, request, pk=None):
            user = self.get_object()
            if self.request.user in user.followers.all():
                return Response({"Followed": f"Already followed {user}"})
            if user.username == request.user.username:
                return Response({"Denied": "You can't follow yourself"})
            
            user.followers.add(self.request.user)
            serializer = self.get_serializer(user)
            return Response({"Detail": f"{request.user} Followed {user}", "Data": serializer.data})
    
    @action(methods=["list"], url_path="followers", detail=True)
    def list_followers(self, request, pk=None):
        """ get all followers who are following a certain user """
        user = self.get_object()
        followers = user.followers.all()
        if not followers:
            return Response({"Detail": "No one is following"})
        serializer = self.get_serializer(followers, many=True)
        return Response(serializer.data)

    @action(methods=["post"], url_path="unfollow_user", detail=True)
    def unfollow_user(self, request, pk=None):
        """ unfollow users """
        user = self.get_object()
        if not user:
            return Response({"Detail": "No user was found"})
        user.followers.remove(request.user)
        return Response({"Unfollowed": f"{request.user} Unfollowed {user}"})
    
    