from django.shortcuts import redirect, render
from accounts.models import Orders
from vehicles.models import Vehicle, VehicleCustom

# Create your views here.
def vehicle_custom(request, vehicle_id):
    vehicles = Vehicle.objects.all()
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'design.html', {'vehicle': vehicle, 'vehicles': vehicles})

def vehicle_checkout(request):
    if not request.user.is_authenticated:
        return redirect("account:signin")
    if request.method == 'POST':
        veh_id = request.POST['veh_id']
        vehicle = Vehicle.objects.get(id=veh_id)
        user = request.user
        custom_wheels = request.POST['wheelOptions']
        custom_color = request.POST['colorOptions']
        custom_interior = request.POST['interiorOptions']
        custom_vehicle = VehicleCustom.objects.create(vehicle_custom_vehicle=vehicle, vehicle_custom_user=user, vehicle_custom_wheels=custom_wheels, vehicle_custom_color=custom_color, vehicle_custom_interior=custom_interior)
        print(custom_vehicle)
        return render(request, 'vehicle_checkout.html', {'vehicle': vehicle, 'custom_vehicle': custom_vehicle})
    return render(request, 'vehicle_checkout.html')

def confirmOrder(request):
    if not request.user.is_authenticated:
        return redirect("account:signin")
    if request.method == 'POST':
        order_user = request.user
        order_vehicle_id = request.POST['custom_veh_id']
        order_vehicle = VehicleCustom.objects.get(id=order_vehicle_id)
        order_total = request.POST['total']
        order = Orders.objects.create(order_user=order_user, order_vehicle=order_vehicle, order_total=order_total)
    return redirect('account:profile')