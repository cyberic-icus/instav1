from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (ListAPIView,
	RetrieveUpdateDestroyAPIView,
	ListCreateAPIView,
	RetrieveAPIView,
	CreateAPIView,
	RetrieveDestroyAPIView,
	RetrieveUpdateAPIView)

from .permissions import *
from .models import CustomUser, Post
from .serializers import *


class UserListView(ListAPIView): 
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
	                                                                                    # Список всех пользователей, без разрешений

class SingleUserUpdateView(RetrieveUpdateAPIView):
	permission_classes = (IsAllowedToUpdate, )
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
	                                                                                    # Обновить данные конкретного пользователя, разрешение на обновление - владелец профиля

class SingleUserView(RetrieveAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
	                                                                                    # Данные конкретного пользователя

class UserPostListView(ListAPIView):
	serializer_class = PostListSerializer
	def get_queryset(self):
		user = self.kwargs['pk']
		return Post.objects.filter(user = user)
	serializer_class = PostListSerializer
                                                                                        # Список постов конкретного полльзователся

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
                                                                                        # Общий список постов(ад)

class PostCreateView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer
	
	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
	                                                                                    # Создать пост, разрешение - залогинился


class SinglePostUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwner, )
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	
	                                                                                    # Конкретный пост, разрешение на изменение - владелец поста
	                                                                                    
class SinglePostView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	
	                                                                                    # Конкретный пост

class SingleUserDeleteView(RetrieveDestroyAPIView):
	permission_classes = (IsAdminUser, )
	queryset = CustomUser.objects.filter(reqdel = True)
	serializer_class = UserSerializer
	                                                                                    # Удаление
