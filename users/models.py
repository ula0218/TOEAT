from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    EXERCISE_CHOICES = [
        ("1", "幾乎不"),
        ("2", "兩週一次"),
        ("3", "一週一次"),
        ("4", "一週三次"),
        ("5", "每天"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10,blank=False,null=True)
    height = models.FloatField(max_length=10,blank=False,null=True)
    weight = models.FloatField(max_length=10,blank=False,null=True)
    exercise = models.CharField(max_length=10,choices=EXERCISE_CHOICES,blank=False)