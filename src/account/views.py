from django.shortcuts import render , redirect ,get_object_or_404
from account.models import Account
from userprofile.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate ,logout , login 
from account.forms import (
    UserRegisterForm,
    UserLoginForm,
    UserUpdateForm
)
import time
# Create your views here.

def account_register_view(request):
    context = {}
    
    if request.method == 'POST':
        print(request.FILES)
        form = UserRegisterForm(request.POST or None  , request.FILES or None)
      
        print('posted')

       
        print(form.errors)
        if form.is_valid():
            print("saved")
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            messages.info(request,"Welcome  {0}" .format(name))
            time.sleep(2)
            return redirect('products:product_list')
        else:
            form.initial = {
                "email"             : request.POST['email'],
                "name"              : request.POST['name'],
                "contact"           : request.POST['contact'],
            }
            context['form'] = form
    else:
        context['form'] = UserRegisterForm()
    
    return render(request ,'account/register.html' ,context )


def account_login_view(request):
    context = {}

    user = request.user

    if user.is_authenticated:
        return redirect("products:product_list")
    
    if request.POST:
        print(request.POST)
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            print(email,password)
            user = authenticate(email = email , password = password)
            if user:
                login(request , user)
                return redirect("products:product_list")
    
    else:
        form = UserLoginForm()
    
    context['login_form'] =form
    return render(request , 'account/login.html' ,context)

def account_logout_view(request):
    logout(request)
    return redirect('login')



def account_update_view(request):
    context = {}

    # code for update acount
    if not request.user.is_authenticated:
        return redirect("login")

    profile = get_object_or_404(Profile , user=request.user)

    if request.POST:
        form = UserUpdateForm(request.POST,instance= request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.initial = {
                "name"              : request.POST['name'],
                "contact"           : request.POST['contact'],
                "date_of_birth"     : request.POST['date_of_birth'],

            }
            
            context['message'] = "Your Account is Updated"
    else:
        form =UserUpdateForm(
            initial = {                
                "name"          : profile.name,
                "contact"       : profile.contact,
                "date_of_birth" : profile.date_of_birth,
                "image"         : profile.image,
            }
        )
    context['update_form'] = form 


    return render(request , 'account/acount.html' , context)


