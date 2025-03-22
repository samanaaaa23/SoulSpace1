from rest_framework import serializers
from .models import Page,Category,BlogPost

class PageSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Page
        fields = '__all__'

class CategorySerialzer(serializers.ModelSerializer) :
    class Meta:
        model = Category
        fields = '__all__'        


class BlogPostSerializer(serializers.ModelSerializer) :
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = BlogPost
        fields = ['id','title','slug','content','author','author_name','category','created_at','updated_at','published']
