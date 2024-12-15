from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm
from vehicles.models import Vehicle
from .models import Orders

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect('account:profile')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('account:profile')
    else:
        form = AuthenticationForm() 
    return render(request, 'signin.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('account:signin')

def profile(request):
    vehicles = Vehicle.objects.all()
    orders = Orders.objects.all()
    if not request.user.is_authenticated:
        return redirect("account:signin")
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            msg = "Password changed successfully!"
        else:
            msg = "Password not changed! Requirements not met."
        return render(request, 'profile.html', {'form': form, 'msg': msg, 'vehicles':vehicles, 'orders':orders})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile.html', {'form': form, 'vehicles':vehicles, 'orders':orders})
