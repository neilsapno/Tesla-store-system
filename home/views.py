from django.shortcuts import render
from vehicles.models import Vehicle

# Create your views here.
def index(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'index.html', {'vehicles': vehicles})