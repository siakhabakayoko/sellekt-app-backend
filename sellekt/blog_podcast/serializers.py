from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, UserProfile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bio', 'avatar', 'followers_count', 'following_count')
        read_only_fields = ('id',)

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at', 'parent', 'replies')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at')

    def get_replies(self, obj):
        if obj.parent is None:  # Only get replies for parent comments
            replies = Comment.objects.filter(parent=obj)
            return CommentSerializer(replies, many=True).data
        return []

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'post_type', 'short_description', 'description',
            'thumbnail', 'video_file', 'audio_file', 'author', 'created_at',
            'updated_at', 'views', 'comments', 'likes_count', 'is_liked'
        )
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'views')

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False

    def validate(self, data):
        post_type = data.get('post_type')
        video_file = data.get('video_file')
        audio_file = data.get('audio_file')
        description = data.get('description')

        if post_type == 'video' and not video_file:
            raise serializers.ValidationError("Video file is required for video posts")
        if post_type == 'audio' and not audio_file:
            raise serializers.ValidationError("Audio file is required for audio posts")
        if post_type == 'text' and not description:
            raise serializers.ValidationError("Description is required for text posts")

        return data
