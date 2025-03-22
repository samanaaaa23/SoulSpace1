from django.db import models

# Create your models here.
from django.db import models

# Category model to categorize the course
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# Author model representing the instructor or author of a course
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Course model representing a course
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='courses')
    duration = models.IntegerField(help_text="Duration in minutes")
    thumbnail = models.ImageField(upload_to='courses/', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(null=True, blank=True)
    order = models.IntegerField(help_text="Order of the lesson in the course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lesson {self.order}: {self.title}"

    class Meta:
        ordering = ['order'] 
