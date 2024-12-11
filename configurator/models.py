from django.db import models
from users.models import User


class Training(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    train_place = models.CharField(max_length = 100)
    train_type = models.CharField(max_length = 100)
    train_program = models.CharField(max_length = 100, null=True, blank=True)
    day_week = models.JSONField(null=True, blank=True)  
    muscle_groups = models.JSONField(null=True, blank=True) 
    difficulty = models.CharField(max_length = 100)  
    train_plan = models.JSONField(null=True, blank=True)


    def __str__(self):
        return self.user.username