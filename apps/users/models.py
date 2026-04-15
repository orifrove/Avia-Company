from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=9)

    def __str__(self):
        return self.phone