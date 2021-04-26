from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('user_name', 'display_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('-created',)
    list_display = ('email', 'user_name', 'display_name','is_active','is_staff')

    fieldsets = (
        ('Account', {'fields': ('user_name', 'display_name', 'email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('about',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'display_name','email', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(User, UserAdminConfig)