from django.urls import path , include
from userprofile.views import my_profile

app_name = 'userprofile'

urlpatterns = [
    path('list/' , my_profile , name = 'profile'),
]
