from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageViewSet, CategoryViewSet, BlogPostViewSet

router = DefaultRouter()
router.register(r'pages', PageViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'blogposts', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
