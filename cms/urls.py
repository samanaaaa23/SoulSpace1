from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageViewSet, CategoryViewSet, BlogPostViewSet,MusicViewSet,PlaylistViewSet,JournalViewSet

router = DefaultRouter()
router.register(r'pages', PageViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'blogposts', BlogPostViewSet)
router.register(r'songs', MusicViewSet)
router.register(r'playlists', PlaylistViewSet, basename='playlist')
router.register(r'journal', JournalViewSet) 


urlpatterns = [
    path('', include(router.urls)),
]