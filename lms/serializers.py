from rest_framework import serializers
from .models import Category, Author, Course, Lesson

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  # List of fields you want to expose in the API

# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio', 'profile_picture']  # Include the fields you want

# Lesson Serializer
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'content', 'video_url', 'order', 'created_at', 'updated_at']

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    # Nested serializers to include related data
    category = CategorySerializer()  # Include category data inside course
    author = AuthorSerializer()      # Include author data inside course
    lessons = LessonSerializer(many=True)  # Include lessons in the course

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'category', 'author', 'duration', 'thumbnail', 'price', 'is_active', 'lessons']
