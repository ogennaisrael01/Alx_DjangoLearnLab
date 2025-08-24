from django.shortcuts import render
from rest_framework import viewsets, generics
from posts.models import Posts, Comments
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from posts.permissions import IsOwner
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import pagination

class PostApiView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title", "content"]
    search_fields = ["title"]
    # pagination_class = [pagination.BasePagination]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer:
            return Response({"Detail": "No data provided"})
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response({
                "Detail": "Post Created",
                "Data": serializer.data,
                },
                status=status.HTTP_201_CREATED)
        else:
            return Response({"Detail": "Invalid serializer object"})
        
    def get_permissions(self):
        if self.action == "update" or "partial_update" or "destroy":
            permission_classes = [permissions.IsAuthenticated(), IsOwner()]

        else:
            permission_classes = [permissions.IsAuthenticated()]
        return permission_classes

    def list(self, request, *args, **kwargs):
        queryset = Posts.objects.all().order_by("-created_at")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def update(self, request, *args, **kwargs):
        post = self.get_object()

        if post:
            serializer = self.get_serializer(post, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response({
                    "Detail": "Post Updated",
                    "Data": serializer.data
                },
                status=status.HTTP_201_CREATED
                )
            else:
                return Response({"Detail": "Serialized object not valid"})
        else:
            return None
    
    def partial_update(self, request, *args, **kwargs):
        post = self.get_object()

        if post:
            serializer = self.get_serializer(post, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(owner=request.user)
                return Response({
                    "Detail": "Post Updated",
                    "Data": serializer.data
                },
                status=status.HTTP_201_CREATED
                )
            else:
                return Response({"Detail": "Serialized object not valid"})
        else:
            return None
        
class CommentCreateApiView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, id=self.kwargs["pk"])
        if post:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(post=post, author=self.request.user)
                return Response({
                    "Detail": f"Comment on {post}",
                    "Data":serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({"Detial": "Serializer not valid"})
        return Response({"Detail": "No post object found"})

class CommentListApiView(generics.ListAPIView):
    """ List associated with any post """
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["post__title"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        """ Retrieving comment in specific post"""
        post = get_object_or_404(Posts, id=self.kwargs["pk"])
        return Comments.objects.filter(post=post).all().order_by("-created_at")
        
   
class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, id=self.kwargs['pk'])
        comment = self.get_object()
        if post:
            serializer = self.get_serializer(comment, data=request.user)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user, post=post)
                return Response({"Data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, id=self.kwargs["pk"])
        comment = self.get_object()
        if post:
            comment.delete()
            return Response({"Detail": "Comment deleted"})
        
    


