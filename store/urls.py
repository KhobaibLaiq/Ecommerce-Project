from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),  # Product detail URL
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('update_cart/<int:product_id>/', update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

]
