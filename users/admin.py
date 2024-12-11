from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_premium', 'is_staff')
    list_filter = ('is_premium', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, UserAdmin)