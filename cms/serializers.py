from rest_framework import serializers
from .models import Page,Category,BlogPost,Song,Playlist,Diary

class PageSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Page
        fields = '__all__'

class CategorySerialzer(serializers.ModelSerializer) :
    class Meta:
        model = Category
        fields = '__all__' 

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'description', 'created_at']  
        read_only_fields = ['id', 'created_at', 'user']

class SongSerialzer(serializers.ModelSerializer) :
    class Meta:
        model = Song
        fields = '__all__'      

class BlogPostSerializer(serializers.ModelSerializer) :
  

    class Meta:
        model = BlogPost
        fields = ['id','title','slug','content','thumbnail','category','created_at','updated_at','published']

class PlaylistSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True)

    class Meta:
        model = Playlist
        fields = '__all__'

    def create(self, validated_data):
        songs = validated_data.pop('songs')
        playlist = Playlist.objects.create(**validated_data)
        playlist.songs.set(songs)
        return playlist

    def update(self, instance, validated_data):
        songs = validated_data.pop('songs', None)
        if songs is not None:
            instance.songs.set(songs)
        instance.playlist_name = validated_data.get('playlist_name', instance.playlist_name)
        instance.preference = validated_data.get('preference', instance.preference)
        instance.save()
        return instance


class PlaylistDetailSerializer(serializers.ModelSerializer):
    songs = SongSerialzer(many=True, read_only=True)  # 🔥 Expand full song data

    class Meta:
        model = Playlist
        fields = ['id', 'playlist_name', 'preference', 'songs']