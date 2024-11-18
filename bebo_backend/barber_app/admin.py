# Use this file to manage models in Django Admin Panel
# http://127.0.0.1:8000/admin/

from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('name', 'email', 'role', 'is_verified', 'created_at')
    
    # Fields to filter by
    list_filter = ('role', 'is_verified')
    
    # Searchable fields
    search_fields = ('name', 'email', 'phone_number')

# Register the User model with the custom admin
admin.site.register(User, UserAdmin)

