# Generated by Django 3.2.3 on 2021-06-09 05:05

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_category_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.FileField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Nisarg/Desktop/Fashionhub/media/{{name}}')),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.FileField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Nisarg/Desktop/Fashionhub/media/{{name}}')),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.FileField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Nisarg/Desktop/Fashionhub/media/{{name}}')),
        ),
    ]