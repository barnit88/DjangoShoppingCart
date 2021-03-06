from django.urls import path , include
from django.contrib.auth import views as auth_views
from account.views import (
    account_register_view,
    account_login_view,
    account_update_view,
    account_logout_view
)




urlpatterns = [
    path('register/' ,account_register_view , name ="register"),
    path('update/' ,account_update_view , name ="update"),
    path('logout/' ,account_logout_view , name ="logout"),
    path('login/' ,account_login_view, name ="login"),
    # path('info/', user_account_info, name= "info"),

 
    path('password_change/done/', auth_views.PasswordChangeDoneView
        .as_view(template_name = "registration/password_change_done.html"),name='password_change_done'),
    
    path('password_change/', auth_views.PasswordChangeView
        .as_view(template_name = "registration/password_change_form.html"),name='password_change'),
   
    path('password_reset/done/', auth_views.PasswordResetDoneView
        .as_view(template_name = "registration/password_reset_done.html"),name='password_reset_done'),
   
    path('password_reset/', auth_views.PasswordResetView
        .as_view() ,name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView
        .as_view(template_name = "registration/password_reset_complete.html"),name='password_reset_complete'),
   
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView
        .as_view(),name='password_reset_confirm'),
   
   

]