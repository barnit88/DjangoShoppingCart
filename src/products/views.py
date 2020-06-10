from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from cart.models import Order
from userprofile.models import Profile

# # Create your views here.
@login_required(login_url = '/account/login')
def product_list(request):
    context = {}
    profile = get_object_or_404(Profile , user=request.user)
    email = request.user.email
    object_list                 = Product.objects.all()
    filtered_order              = Order.objects.filter(owner= request.user.profile ,is_ordered=False)
    current_order_products      = []
    if filtered_order.exists():
        user_order              = filtered_order[0]
        user_order_items        = user_order.items.all()
        current_order_products  = [products.product for products in user_order_items]

    context = {
        'object_list' : object_list ,
        'current_order_products' : current_order_products,
        'profile' : profile,
        'email'     : email
    }

    # messages.info(request , "Hello checking Mesages")
    return render(request,'products/product_list.html' , context)
    

