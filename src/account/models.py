from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self , email , password = None ):
        if not email:
            raise ValueError("Email is required ")
        
        user = self.model(
            email   = self.normalize_email(email),    
        )
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self , email , password ):
        user = self.create_user(
            email       = self.normalize_email(email),
            password    = password ,
        )
        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.save(using = self._db)
        return user 



class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email" , max_length=60 , unique=True)
    date_joined     = models.DateTimeField(verbose_name="date_joined" , auto_now_add=True)    
    last_login      = models.DateTimeField(verbose_name='last login' , auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default = False)

    objects = AccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self,perm , obj = None):
        return True

    def has_module_perms(self,app_label):
        return True






