from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
    
class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Mood(models.Model):
    title = models.CharField(max_length=50)
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    song_file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.song_name


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100)
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE, null=True, blank=True)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlist_name



class Diary(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'cms_journalentry'


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    # Removed author
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
