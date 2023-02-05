from django.urls import path
from .views import product_list, product_detail

#! NB normally when we define an API endpoint, we should add the api/ as prefix --> but best practice to do it in the main urls.py file
urlpatterns = [
    path("products/", product_list, name="product-list"),
    #! NB then you have to go to http://127.0.0.1:8000/api/products/ to see the JSON object resulting
    path("products/<int:pk>/", product_detail, name="product-detail"),
]

"""
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="products-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products-detail"),
]
"""
