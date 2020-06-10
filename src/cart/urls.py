from django.urls import path 

from cart.views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    # success
)

app_name = 'cart'

urlpatterns = [
    path('addtocart/<int:item_id>' , add_to_cart , name="add_to_cart"),
    path('ordersummary' , order_details , name="order_summary"),
    path('delete/<int:item_id>' , delete_from_cart , name="delete"),
    path('checkout/' , checkout , name="checkout"),
    path('transaction/' , update_transaction_records, name="train"),

]

