from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def first_50():
        return self.content[:50]

class user_profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname=models.CharField(max_length=10 ,blank=True)
    date_of_birth=models.DateField()
    profile_photo=models.ImageField(upload_to='profiles', blank=True)
