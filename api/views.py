from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from . import serializers
from .models import Comment, Profile, Post
from rest_framework.permissions import AllowAny


class CreateUserView(generics.GenericAPIView):
    serializer_class = serializers.UserSirializer
    # jwtを上書きして誰でもアクセスできるようにしている
    permission_classes = (AllowAny,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(userProfile=self.request.user)


class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(userProfile=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(userPost=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.Comment

    def perform_create(self, serializer):
        serializer.save(userComment=self.request.user)
