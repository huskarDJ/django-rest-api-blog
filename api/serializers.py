from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'post_set']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comment_set', 'categories']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']

class UserSerializer(serializers.ModelSerializer):
    post_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'post_set', 'comment_set', 'category_set']
