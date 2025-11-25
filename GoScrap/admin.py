from django.contrib import admin
from .models import PickupRequest

# Register your models here.

@admin.register(PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'pickup_date', 'pickup_time', 'status', 'created_at']
    list_filter = ['status', 'pickup_date', 'created_at']
    search_fields = ['name', 'email', 'phone', 'pickup_address']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
