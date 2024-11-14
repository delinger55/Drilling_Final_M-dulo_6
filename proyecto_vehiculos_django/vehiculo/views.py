from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView 
from django.contrib.auth.models import Permission
from .forms import VehiculoForm, RegistroForm
from .models import Vehiculo


# Create your views here.
def vehiculos(request):
    return render(request, 'vehiculo/vehiculos.html')

def index(request):
    vehiculos = Vehiculo.objects.all()  # Obtén todos los vehículos
    return render(request, 'vehiculo/index.html', {'vehiculos': vehiculos})

def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después de guardar
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add.vehiculo.html', {'form': form})

#@login_required
#@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Asigna el permiso al nuevo usuario
            permiso = Permission.objects.get(codename='visualizar_catalogo')
            usuario.user_permissions.add(permiso)
            return redirect('listar')  # Cambia esto a url q se necesita antes listar
    else:
        form = RegistroForm()
    return render(request, 'vehiculo/registro.html', {'form': form})
    

class CustomLoginView(LoginView): 
    template_name = 'vehiculo/login.html'
    
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige a la URL que muestra el mensaje de logout

def logout_message(request):
    return render(request, 'vehiculo/logout.html')    
