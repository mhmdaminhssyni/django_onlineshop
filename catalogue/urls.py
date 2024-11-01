from catalogue.views import products_list, product_detail, category_products, products_search
from django.urls import path, include
urlpatterns = [
    path('product/list/', products_list, name='product-list'),
    path('product/detail/<int:pk>/', product_detail, name='product-detail'),
    path('category/<int:pk>/products/', category_products, name='category-products'),
    path('product/search/', products_search, name='product_search')
]