from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    phone_no = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to= 'images')
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)

#One-to-one relationship maps user with his phone number and profile pic




