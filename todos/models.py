# models.py

from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    TYPES_CHOICES = [
        ("1", "早餐"),
        ("2", "午餐"),
        ("3", "晚餐"),
        ("4", "宵夜"),
        ("5", "零食"),
    ]
    HUNGRY_CHOICES = [
        ("1", "完全沒飽"),
        ("2", "三分飽"),
        ("3", "五分飽"),
        ("4", "七分飽"),
        ("5", "超級飽"),
    ]
    CATEGORY_CHOICES = [
        ("1", "五榖根莖類"),
        ("2", "蔬菜類"),
        ("3", "水果類"),
        ("4", "蛋豆魚肉類"),
        ("5", "奶類"),
        ("6", "油脂類"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, choices=TYPES_CHOICES)
    hungry = models.CharField(max_length=10, choices=HUNGRY_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    food = models.CharField(max_length=200, null=True, blank=True)
    category = models.ManyToManyField('Category', related_name='todos')
    directions = models.CharField(max_length=200, null=True, blank=True)

class Category(models.Model):
    CATEGORY_CHOICES = [
        ("1", "五榖根莖類"),
        ("2", "蔬菜類"),
        ("3", "水果類"),
        ("4", "蛋豆魚肉類"),
        ("5", "奶類"),
        ("6", "油脂類"),
    ]
    name = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

