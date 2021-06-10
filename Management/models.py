from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, blank=True)
    mob = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    cat = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name + ' <-----> ' + str(self.cat.title)

class Product(models.Model):
    sub_cat = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True, blank=True)
    img1 = models.FileField(null=True,upload_to=settings.MEDIA_ROOT / 'product_images',blank=True)
    img2 = models.FileField(null=True,upload_to=settings.MEDIA_ROOT / 'product_images',blank=True)
    img3 = models.FileField(null=True,upload_to=settings.MEDIA_ROOT / 'product_images',blank=True)
    discription = models.TextField(null=True, blank=True)
    mrp = models.FloatField(null=True, blank=True)
    sp = models.FloatField(null=True, blank=True)
    available = models.BooleanField(null=True, blank=True, default=True)

    def __str__(self):
        return self.name + ' <--> ' + str(self.sub_cat.name) + ' <--> ' + str(self.sub_cat.cat.title)


class ContactForm(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name