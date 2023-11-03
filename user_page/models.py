from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phonenumber = models.CharField(max_length=15, default="Unknown")
    country = models.CharField(max_length=100, default="Unknown")
    password = models.CharField(max_length=128)
    avatar = models.TextField()
    role = models.CharField(max_length=50, default='user')
    
    def __str__(self):
        return self.username

