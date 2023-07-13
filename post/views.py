from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .permissions import IsAuthorOrAdmin, IsAuthor
from .serializers import PostCreateSerializer, PostListSerializers, PostDetailSerializer


# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return PostListSerializers


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsAuthorOrAdmin(),
        elif self.request.method in ['PUT', 'PATCH']:
            return IsAuthor(),
        return permissions.AllowAny(),

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostCreateSerializer
        return PostDetailSerializer
