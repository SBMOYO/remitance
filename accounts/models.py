from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    surname = models.CharField(_('surname'), max_length=30, blank=True)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    identification_number = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    residential_address = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'surname', 'identification_number', 'phone_number', 'residential_address']   

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.surname} {self.email}"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True