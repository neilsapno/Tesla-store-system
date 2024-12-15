from django.contrib import admin
from .models import Vehicle, VehicleCustom

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'vehicle_range', 'vehicle_topspeed', 'vehicle_acceleration', 'vehicle_price', 
    'vehicle_home_image', 'vehicle_image_1', 'vehicle_image_1_name', 'vehicle_image_2', 'vehicle_image_2_name', 'vehicle_image_3', 'vehicle_image_3_name', 'vehicle_image_4', 'vehicle_image_4_name',
    'vehicle_wheel_1_image', 'vehicle_wheel_1_name', 'vehicle_wheel_2_image', 'vehicle_wheel_2_name')

class VehicleCustomAdmin(admin.ModelAdmin):
    list_display = ('vehicle_custom_vehicle', 'vehicle_custom_user', 'vehicle_custom_wheels', 'vehicle_custom_color', 'vehicle_custom_interior')
    list_filter = ('vehicle_custom_user', 'vehicle_custom_vehicle')
    search_fields = ('vehicle_custom_user', 'vehicle_custom_vehicle')

admin.site.register(VehicleCustom, VehicleCustomAdmin)
admin.site.register(Vehicle, VehicleAdmin)
