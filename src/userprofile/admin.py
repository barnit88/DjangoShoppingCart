from django.contrib import admin
from userprofile.models import Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ProfileAdminSite(admin.ModelAdmin):
    list_display        = ( 'user' , 'name' , 'contact' , 'date_of_birth' , 'image' )
    search_fields       = ['name'  , 'contact']
    ordering            = ['name',]
    list_filter         = ()
    fieldsets           = (
    
    )
    add_fieldsets       = (
        (None , {
            'classes'   : ('wide' ,) ,
            'fields'    : ( 'user' , 'name' , 'contact' , 'date_of_birth' , 'image' )
        }),
    )

    filter_horizontal = ()


admin.site.register(Profile, ProfileAdminSite)


