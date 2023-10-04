from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , Details

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file_path')

admin.site.register(Details, DetailsAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
