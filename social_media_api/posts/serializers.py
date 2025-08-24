from rest_framework import serializers
from posts.models import Comments, Posts
from django.utils import timezone

class CommentSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.ReadOnlyField(source="post.title")
    class Meta:
        model = Comments
        fields = ["post", "author", "content", "days_since_created"]

    def get_days_since_created(self, obj):
        """ Get the days the comment was made"""
        now = timezone.now()
        days = now - obj.created_at
        if days:
            return f'{days.days} day(s) ago'
        return serializers.ValidationError("Cant find the actual date")
    def validate_content(self, value):
        if value:
            return value
        return serializers.ValidationError("No contents are provided")

class PostSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source="author.username")
    
    class Meta:
        model = Posts
        fields = ["id", "title", "author", "content", "days_since_created", "comments"]

    def get_days_since_created(self, obj):
        """ Get the days the comment was made"""
        now = timezone.now()
        days = now - obj.created_at
        if days:
            return f'{days.days} day(s) ago'
        return serializers.ValidationError("Cant find the actual date")
    
    def create(self, validated_data):
        return Posts.objects.create(**validated_data)
    

    