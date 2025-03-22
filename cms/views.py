from django.shortcuts import render
from rest_framework import viewsets
from .models import Page, Category, BlogPost
from .serializers import PageSerializers, CategorySerialzer, BlogPostSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Pages.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Blog Posts.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    