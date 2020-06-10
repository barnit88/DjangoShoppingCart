from django.urls import path , include
from products.views import product_list

app_name = 'products'

urlpatterns = [
    path('list/' , product_list , name = 'product_list'),
]
