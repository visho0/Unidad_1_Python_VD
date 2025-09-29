from django.contrib import admin
from .models import(
    Category, Product, AlertRule, ProductAlertRule,
    Zone, Device, Measurement, AlertEvent
)

# Register your models here.
admin.site.site_header = "EcoEnergy - Admin"
admin.site.site_title = "EcoEnergy Admin"
admin.site.index.title = "Panel de administración"

# MAESTROS (globales)

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")
    search_fields = ("name",)
    list_filter = ("status",)
    ordering = ("name",)
    list_per_page = 50
