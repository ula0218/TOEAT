# Generated by Django 5.0.6 on 2024-06-04 13:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0005_alter_todo_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="user",
        ),
    ]