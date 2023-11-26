

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=20,null=True,blank=True )
    email_active_code = models.EmailField(max_length=100, null=True,blank=True)


    def __str__(self):
        return self.get_full_name()


