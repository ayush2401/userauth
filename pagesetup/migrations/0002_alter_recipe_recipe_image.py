# Generated by Django 4.1.10 on 2023-08-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(upload_to='recipes'),
        ),
    ]