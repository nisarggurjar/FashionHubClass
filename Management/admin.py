from django.contrib import admin
from .models import *

admin.site.register(UserDetail)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ContactForm)
admin.site.register(Payment_ids)