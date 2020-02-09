from django.urls import path, include
from .views import *

app_name = 'users'
urlpatterns = [
   path('', UserListView.as_view()), 
   path('<int:pk>/', SingleUserView.as_view()), 
   path('<int:pk>/update', SingleUserUpdateView.as_view()),
   path('<int:pk>/posts/', UserPostListView.as_view()), 
   path('posts/', PostListView.as_view()), 
   path('posts/create', PostCreateView.as_view()), 
   path('posts/<int:pk>', SinglePostView.as_view()), 
   path('posts/<int:pk>/update', SinglePostUpdateDestroyView.as_view()), 
   path('admin/delete-users/<int:pk>', SingleUserDeleteView.as_view())
] 