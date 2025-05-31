from rest_framework import serializers
from .models import Category, Author, Course, Lesson,SubCategory,Order

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description'] 

class SubCategorySerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to handle category as an ID (integer)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'category']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio', 'profile_picture']  





class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'  # or specify only the fields you need

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__' 


class CategoryWithCoursesSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'subcategories', 'courses']


class OrderSerializer(serializers.ModelSerializer):
    course_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'course_id', 'course_title', 'price', 'is_paid', 'payment_token', 'created_at', 'course_thumbnail']

    def get_course_thumbnail(self, obj):
        from lms.models import Course 
        try:
            course = Course.objects.get(id=obj.course_id)
            return course.thumbnail.url if course.thumbnail else None
        except Course.DoesNotExist:
            return None