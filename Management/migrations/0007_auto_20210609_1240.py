# Generated by Django 3.2.3 on 2021-06-09 07:10

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0006_auto_20210609_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.FileField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Nisarg/Desktop/Fashionhub/media/product_images')),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.FileField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Nisarg/Desktop/Fashionhub/media/product_images')),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.FileField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Nisarg/Desktop/Fashionhub/media/product_images')),
        ),
    ]