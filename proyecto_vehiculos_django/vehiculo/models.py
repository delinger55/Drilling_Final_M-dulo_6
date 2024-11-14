from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    condicion_precio = models.CharField(max_length=10, blank=True, editable=False)  # Nuevo campo, solo para lectura

    def save(self, *args, **kwargs):
        # Asignar condición de precio basado en el precio
        if self.precio < 10000:
            self.condicion_precio = 'Bajo'
        elif 10000 <= self.precio <= 30000:
            self.condicion_precio = 'Medio'
        else:
            self.condicion_precio = 'Alto'
        
        super().save(*args, **kwargs)
        
        
    #class Meta:
        #permissions = [
            #("visualizar_catalogo", "Puede visualizar el catálogo de vehículos"),
        #]


    def __str__(self):
        return f"{self.marca} - {self.modelo}"
