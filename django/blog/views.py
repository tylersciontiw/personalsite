from django.shortcuts import render

# todos/views.py
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer