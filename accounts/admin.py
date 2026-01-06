from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    
    list_display = ['username', 'email', 'role', 'first_name', 'last_name', 'is_active', 'created_at']
    list_filter = ['role', 'is_active', 'is_staff', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'company_name']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Login Info', {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'profile_picture')
        }),
        ('Role & Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Employer Info', {
            'fields': ('company_name', 'company_website'),
            'classes': ('collapse',), 
        }),
        ('Job Seeker Info', {
            'fields': ('skills', 'experience_years'),
            'classes': ('collapse',),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'first_name', 'last_name'),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'last_login', 'date_joined']
    
    actions = ['make_active', 'make_inactive']
    
    def make_active(self, request, queryset):
        
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} user(s) activated successfully.')
    make_active.short_description = "Activate selected users"
    
    def make_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} user(s) deactivated successfully.')
    make_inactive.short_description = "Deactivate selected users"