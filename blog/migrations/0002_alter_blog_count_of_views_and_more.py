# Generated by Django 5.1.1 on 2024-09-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="count_of_views",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="blog",
            name="publication_sign",
            field=models.BooleanField(default=True),
        ),
    ]
