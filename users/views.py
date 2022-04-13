from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm
from .models import User

# Create your views here.
def home(request):
    return render(request,'users/home.html')


def buyer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        
        
        
        new_user = User(username=username, email=email, password=make_password(password1), is_buyer=True)

        form = RegisterForm(request.POST, instance=new_user)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have registered. Sign In')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form':form})


# seller registration
def seller_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        
        
        new_user = User(username=username, email=email, password=make_password(password1), is_seller=True)

        form = RegisterForm(request.POST, instance=new_user)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have registered. Sign In')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form':form})

