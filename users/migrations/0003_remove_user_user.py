# Generated by Django 5.0.6 on 2024-06-04 13:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="user",
        ),
    ]
