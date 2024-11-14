from django.urls import path #include
from . import views

urlpatterns = [
    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('', views.index, name='index'),
    path('add/', views.add_vehiculo, name='add_vehiculo'),
    path('listar/', views.listar, name= 'listar'),
    path('registro/', views.registrar_usuario, name='registro'), 
    #path('accounts/', include('django.contrib.auth.urls')),  # Agrega las URLs de autenticación de Django
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-message/', views.logout_message, name='logout_message'),  # Muestra el mensaje de cierre de sesión
]

    
