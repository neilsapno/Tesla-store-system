from django.urls import path
from . import views

app_name = "vehicle"

urlpatterns = [
    path('vehicle/<int:vehicle_id>/design', views.vehicle_custom, name='vehicle_custom'),
    path('vehicle/checkout', views.vehicle_checkout, name='vehicle_checkout'),
    path('confirmOrder/', views.confirmOrder, name="confirmOrder")
]
