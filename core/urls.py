from django.urls import path, include

from .views import index, product, contact

urlpatterns = [
    path('', index, name='index'),
    path('product', product, name='product'),
    path('contact', contact, name='contact'),
]
