from rest_framework import serializers
from .models import CustomUser, Post



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'photo')
		
class PostCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'body', 'pic_desc', 'image', 'tags' )
		
class PostListSerializer(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)
	class Meta:
		model = Post
		fields = ('user', 'title', 'body', 'pic_desc', 'image', 'tags')

class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'body', 'pic_desc', 'image', 'tags')
		

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id', 'title', 'body', 'pic_desc', 'image', 'tags')