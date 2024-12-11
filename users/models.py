from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_premium = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return self.username