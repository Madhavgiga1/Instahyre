from django.db import models
from django.contrib.auth import (get_user_model)
# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
   

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Enter phone number first please')
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
    
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_number, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
   
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number.as_e164
    
#This stores spam reports made my users
class Spam(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = PhoneNumberField()
    reporting_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "{name} reported {phone}".format(
            name=self.reporting_user.get_full_name() if self.reporting_user else 'Deleted User',
            phone=self.phone_number
        )
    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)  
    phone_number = PhoneNumberField()
    associated_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
       return self.name