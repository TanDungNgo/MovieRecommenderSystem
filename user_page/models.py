from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='img/')
    role = models.CharField(max_length=50, default='user')
    
    def __str__(self):
        return self.username

