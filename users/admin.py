from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User



@admin.register(User)
class MyUserAdmin(UserAdmin):
    filter_horizontal = ('groups', 'user_permissions')
    model = User
    ordering = ('email',)
    list_display = ['email', 'username', 'phone', 'tg_name', 'country']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', )}),
        ('Additional info', {'fields': ('phone', 'tg_name', 'country')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


