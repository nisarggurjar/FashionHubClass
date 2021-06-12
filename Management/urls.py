from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', Contact, name='contact'),
    path('about/', About, name='about'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
    
]