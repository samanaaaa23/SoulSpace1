from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AuthorViewSet, CourseViewSet,initiate_khalti_payment,khalti_lookup,create_order, user_orders,LessonViewSet,SubCategoryViewSet,CategoryWithCoursesView

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categorywithcourse/<int:pk>/', CategoryWithCoursesView.as_view(), name='category-with-courses'),
    path('create-order/', create_order, name='create_order'),
    path("khalti/initiate/", initiate_khalti_payment),
    path("khalti/lookup/", khalti_lookup),
    path('orders/my-orders/', user_orders),

   
]
