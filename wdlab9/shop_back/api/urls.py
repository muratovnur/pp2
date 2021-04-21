from django.urls import path
from api.views import products_list, product_details, categories_list, category_details

urlpatterns = [
    path('products/', products_list),
    path('products/<int:product_id>/', product_details),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', category_details)
]
