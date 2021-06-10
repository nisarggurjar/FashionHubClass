# Generated by Django 3.2.3 on 2021-06-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0007_auto_20210609_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
