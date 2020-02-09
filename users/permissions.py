from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    def filter(self, rest_permissions, filtered_queryset,
               user, action):
        yield filtered_queryset.filter(owner=user)
        
        
class IsAllowedToUpdate(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.id == request.user.id