from django.shortcuts import render ,redirect ,get_object_or_404 
from userprofile.models import Profile
from products.models import Product
from cart.models import Order , OrderItem , Transaction
from django.contrib import messages
import datetime


def get_user_pending_order(request):
    profile = get_object_or_404(Profile,user=request.user)
    order   = Order.objects.filter(owner=profile , is_ordered=False)
    if order.exists():
        return order[0]
    return 0

def add_to_cart(request , **kwargs):
    context = {}
    # get User Profile
    profile = get_object_or_404(Profile, user=request.user)
    #filtered by produc id
    product = Product.objects.filter(pk=kwargs.get('item_id' , "")).first()
    
    #create order item 
    order_item , status = OrderItem.objects.get_or_create(product = product,owner=profile)
    # create order associated with user
    user_order, status = Order.objects.get_or_create(owner=profile)
    if order_item.owner.user.email == user_order.owner.user.email:
        user_order.items.add(order_item)
    
    if status:
        user_order.save()
    
    messages.info(request, "Item added to Cart ")
    return redirect('products:product_list')

def order_details(request):
    context = {}
    orders = get_user_pending_order(request)
    context['orders'] = orders
    return render(request,'cart/order_summary.html' , context)

def delete_from_cart(request , item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    
    # print(item_to_delete.owner.user.email)
    if item_to_delete.exists():
        delete_item = item_to_delete[0]

        if request.user.email == delete_item.owner.user.email:
            delete_item.delete()
            messages.info(request,"Your item has been deleted from cart")
    
    return redirect('cart:order_summary')

def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order' : existing_order
    }
    return render(request, 'cart/new_checkout.html' , context)

def update_transaction_records(request):
    #pulling out order
    order_to_purchase = get_user_pending_order(request)
    order_to_purchase.is_ordered = True
    order_to_purchase.date_ordered = datetime.datetime.now()
    order_to_purchase.save()
    #pulled order updated and saved it by making some changes 

    #querring items list 
    order_items = order_to_purchase.items.all()

    #updating queried list all at once
    order_items.update(is_ordered= True ,date_ordered = datetime.datetime.now())

    user_profile = get_object_or_404(Profile, user=request.user)
    
    
    # get the products from the items
    # Yo chai list ekaichoti add garney tarika ho hai 
    #just for memo
    # order_products = [item.product for item in order_items]
    # user_profile.ebooks.add(*order_products)
    # user_profile.save()
    transaction = Transaction(profile=user_profile,
                            order_id=order_to_purchase.id,
                            amount=order_to_purchase.get_cart_total(),
                            success=True)

    transaction.save()

    messages.info(request,"Thank You from buying from our site")
    return redirect('userprofile:profile')


