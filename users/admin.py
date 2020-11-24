from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User
from django.utils.translation import ugettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),

        ("Personal information", {"fields": ("first_name", "last_name")}),

        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),

        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('phone_number', 'id', 'is_active', 'is_staff', 'is_superuser',)

    search_fields = ('is_active', 'is_staff', 'is_superuser',)
    ordering = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
