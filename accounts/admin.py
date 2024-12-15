from django.contrib import admin
from .models import Orders

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_user', 'order_vehicle', 'order_date', 'order_time', 'order_total')
    list_filter = ('order_user', 'order_vehicle', 'order_date', 'order_time', 'order_total')
    search_fields = ('order_user', 'order_vehicle')
    ordering = ('order_user', 'order_vehicle', 'order_date', 'order_time', 'order_total')

admin.site.register(Orders, OrdersAdmin)