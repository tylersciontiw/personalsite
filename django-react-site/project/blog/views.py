from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import generics

class PostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Create your views here.
