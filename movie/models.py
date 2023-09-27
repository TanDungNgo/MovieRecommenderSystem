from django.db import models

# Create your models here.
class Phim(models.Model):
    ten_phim = models.CharField(max_length=100)
    mo_ta = models.TextField()
    nam_san_xuat = models.IntegerField()
    hinh_anh = models.ImageField(upload_to='hinh_phim/')
