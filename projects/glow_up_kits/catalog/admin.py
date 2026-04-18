from django.contrib import admin

from .models import Kit, Order


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "sale_price", "cost", "stock_qty", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "sku", "contents")
    ordering = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "kit", "quantity", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer_name", "kit__name", "notes")
    ordering = ("-created_at",)
