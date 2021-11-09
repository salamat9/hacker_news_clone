from rest_framework import serializers

from .models import Post, Comment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'created', 'post')


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    upvotes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author', 'comments', 'upvotes')


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author')


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    upvotes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author', 'comments', 'upvotes')

