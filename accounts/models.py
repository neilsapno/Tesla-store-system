from django.db import models
from vehicles.models import VehicleCustom

# Create your models here.
class Orders(models.Model):
    order_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_vehicle = models.ForeignKey(VehicleCustom, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_payment = models.CharField(max_length=200, default="Card")