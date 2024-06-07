# Generated by Django 5.0.6 on 2024-06-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_record_delete_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="height",
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="name",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="weight",
            field=models.FloatField(max_length=10, null=True),
        ),
    ]