from django.contrib import admin
from django.urls import path
from .views import product_list, product_detail, manufacturer_list, manufacturer_detail


urlpatterns = [
    path('products/', product_list,name="product-list"),
    path('manufacturers/', manufacturer_list,name="manufacturer-list"),
    path('products/<int:pk_product>', product_detail,name="product-detail"),
    path('manufacturers/<int:pk_manufacturer>', manufacturer_detail,name="manufacturer-detail"),
]
