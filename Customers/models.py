from django.db import models
from django.contrib.auth.models import User
from Management.models import *

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' <--> ' + self.product.name