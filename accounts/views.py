from django.shortcuts import render, redirect  # Se agregó 'redirect' para redirigir correctamente
from .forms import RegistrationForm  # Asegúrate de que esta importación sea correcta
from .models import Account
from django.contrib import auth  # Importar 'auth' correctamente para autenticación
from django.contrib.auth import logout as auth_logout  # Para evitar conflicto de nombres
from django.contrib.auth import login as auth_login  # Para usar la función de login de Django

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Corregir typo en 'form.cleaned_data' en lugar de 'form_cleaned_data'
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            
            # Crear usuario con los datos proporcionados
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password
            )
            user.phone_number = phone_number  # Asignar número de teléfono
            user.save()  # Guardar el usuario
            
            # Redirigir a una página después del registro (opcional, puedes ajustar según tu flujo)
            return redirect('login')  # Redirigir a la página de login o a donde prefieras
    else:
        form = RegistrationForm()  # Si no es POST, se muestra el formulario vacío
    
    return render(request, 'register.html', context={'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")  # Se utiliza 'get' para evitar posibles errores si la clave no está
        password = request.POST.get("password")
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth_login(request, user)  # Usar 'auth_login' en lugar de 'auth.login'
            return redirect('home')  # Redirigir a la página de inicio o donde prefieras
        else:
            return redirect('login')  # Si no se autentica, redirigir al login
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)  # Usar 'auth_logout' para cerrar sesión correctamente
    return redirect('login')  # Redirigir a la página de login después de cerrar sesión



