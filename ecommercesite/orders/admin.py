from django.contrib import admin
from .models import Order,OrderItem

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    row_id_fields=["product"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=["id","full_name","email"]
    inlines =[OrderItemInLine]
    readonly_fields=("created_at",)

