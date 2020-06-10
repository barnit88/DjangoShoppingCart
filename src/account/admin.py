from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AdminSite(UserAdmin):
    list_display        = ( 'email' , 'date_joined' , 'last_login' , 'is_staff' , 'is_admin' )
    search_fields       = ( 'email', )
    ordering            = ('email',)
    list_filter         = ()
    fieldsets           = (

    )
    add_fieldsets       = (
        (None , {
            'classes'   : ('wide' ,) ,
            'fields'    : ('email' , 'password1' , 'password2' )
        }),
        ('Permissions' , {
            'fields'    : ('is_staff' , 'is_siperuser' , 'is_admin' , 'is_active')
        }),
    )

    filter_horizontal = ()


admin.site.register(Account, AdminSite)

