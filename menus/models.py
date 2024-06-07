from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('1', '台式'),
        ('2', '美式'),
        ('3', '日式'),
        ('4', '義式'),
        ('5', '健康餐'),
        ('6', '隨機'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, null=True)