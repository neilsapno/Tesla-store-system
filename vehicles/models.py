from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=255)
    vehicle_range = models.CharField(max_length=10)
    vehicle_topspeed = models.CharField(max_length=10)
    vehicle_acceleration = models.CharField(max_length=10)
    vehicle_price = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_home_image = models.URLField()
    vehicle_image_1 = models.URLField()
    vehicle_image_1_name = models.CharField(max_length=100)
    vehicle_image_2 = models.URLField()
    vehicle_image_2_name = models.CharField(max_length=100)
    vehicle_image_3 = models.URLField()
    vehicle_image_3_name = models.CharField(max_length=100)
    vehicle_image_4 = models.URLField()
    vehicle_image_4_name = models.CharField(max_length=100)
    vehicle_wheel_1_image = models.URLField()
    vehicle_wheel_1_name = models.CharField(max_length=100)
    vehicle_wheel_2_image = models.URLField()
    vehicle_wheel_2_name = models.CharField(max_length=100)

class VehicleCustom(models.Model):
    vehicle_custom_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_custom_user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_custom_wheels = models.CharField(max_length=255)
    vehicle_custom_color = models.CharField(max_length=255)
    vehicle_custom_interior = models.CharField(max_length=255)