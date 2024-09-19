from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import auth
from django.contrib.auth import logout as auth_logout, login as auth_login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password
            )
            user.phone_number = phone_number
            user.save()

            return redirect('login')  # Redirige a la página de login
    else:
        form = RegistrationForm()  # Muestra el formulario vacío

    return render(request, 'register.html', context={'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Autenticación por email y contraseña
        user = auth.authenticate(username=email.split("@")[0], password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirige a la página de inicio
        else:
            return redirect('login')  # Redirige al login en caso de error
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirige a la página de login después de cerrar sesión
