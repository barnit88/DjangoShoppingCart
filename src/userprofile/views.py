from django.shortcuts import render
from userprofile.models import Profile
from cart.models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.


def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders
	}

	return render(request, "userprofile/profile.html", context)


