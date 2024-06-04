from django.db import models


class User(models.Model):
    EXERCISE_CHOICES = [
        ("1", "幾乎不"),
        ("2", "兩週一次"),
        ("3", "一週一次"),
        ("4", "一週三次"),
        ("5", "每天"),
    ]
    name = models.CharField(max_length=10,null=True, blank=True)
    height = models.FloatField(max_length=10,null=True, blank=True)
    weight = models.FloatField(max_length=10,null=True, blank=True)
    exercise = models.CharField(max_length=10,choices=EXERCISE_CHOICES)