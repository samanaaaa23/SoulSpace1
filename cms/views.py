from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Page, Category, BlogPost,Song,Playlist,Diary
from .serializers import PageSerializers, CategorySerialzer,PlaylistSerializer, BlogPostSerializer,SongSerialzer,PlaylistDetailSerializer,JournalSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
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

class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Diary.objects.all()  # ✅ Add this line back

    def get_queryset(self):
        return Diary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MusicViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Blog Posts.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerialzer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    @action(detail=True, methods=['get'], url_path='detailsplaylist')
    def detailsplaylist(self, request, pk=None):
        playlist = self.get_object()  # get playlist by ID
        serializer = PlaylistDetailSerializer(playlist)
        return Response(serializer.data)
    