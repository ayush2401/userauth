# Generated by Django 4.1.10 on 2023-08-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_description', models.CharField(max_length=300)),
                ('recipe_image', models.ImageField(upload_to='recipe')),
            ],
        ),
    ]