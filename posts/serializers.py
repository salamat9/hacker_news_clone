from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author')


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author')


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author')

