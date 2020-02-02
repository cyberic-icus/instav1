from django.db import models
from django.contrib.auth.models import AbstractUser
from instav1 import settings

class CustomUser(AbstractUser):
	name = models.CharField(blank = True, max_length = 100)
	photo = models.ImageField(upload_to = 'images/userpics', default = 'media/images/userpics/default.jpg')
	reqdel = models.BooleanField(default = False)
	
	def __str__(self):
		return self.email

		
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.TextField(null=True, blank=True)
    pic_desc = models.CharField(max_length=100, null = True)
    image = models.ImageField(upload_to = 'images/postpics', blank = True, null=True)
    
    def __str__(self):
    	return self.title
