from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Crear el modelo de la tabla que corresponda con cada entidad de la Base de Datos
# clase que contiene el diseño de la tabla CAT_EQUIPO
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils.functional import cached_property


class Cat_Equipo(models.Model):
    modelo_equipo = models.CharField(max_length=100)
    marca_equipo = models.CharField(max_length=100)
    num_serie_equipo = models.CharField(max_length=100)
    num_parte_equipo = models.CharField(max_length=100)
    procesador_equipo = models.CharField(max_length=100)
    ram_equipo = models.CharField(max_length=100)
    disco_equipo = models.CharField(max_length=100)
    comentario_equipo = models.CharField(max_length=500)
    activo_equipo = models.BooleanField(default=True)

    # Metodo STR regresa una cadena que muestra las columnas que apareceran referenciando a
    # cada clase en el panel de administracion de Django
    def __str__(self):
        return f'Equipo {self.id}: {self.marca_equipo} {self.modelo_equipo}'


# clase que contiene el diseño de la tabla CAT_CLIENTE
class Cat_Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellidos_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    correo_cliente = models.EmailField(max_length=50)
    celular_cliente = models.CharField(max_length=10)
    activo_cliente = models.BooleanField(default=True)

    # Metodo STR regresa una cadena que muestra las columnas id|nombre|apellidos
    # En el panel de administracion Django
    def __str__(self):
        return f'Cliente {self.id} {self.nombre_cliente} {self.apellidos_cliente}'


# clase que contiene el diseño de la tabla CAT_SERVICIO
class Cat_Servicio(models.Model):
    sku_servicio = models.CharField(max_length=50)
    tipo_servicio = models.CharField(max_length=50)
    descripcion_servicio = models.CharField(max_length=500)
    costo_servicio = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    activo_servicio = models.BooleanField(default=True)

    # Metodo STR regresa una cadena que muestra las columnas id|descripcion
    def __str__(self):
        return f'Servicio {self.id} {self.tipo_servicio}'


# clase que contiene el diseño de la tabla CAT_PRODUCTO
class Cat_Producto(models.Model):
    sku_producto = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50)
    descripcion_producto = models.CharField(max_length=500)
    costo_producto = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    activo_producto = models.BooleanField(default=True)

    # Metodo STR regresa una cadena que muestra las columnas id|descripcion
    def __str__(self):
        return f'Producto {self.id} {self.tipo_producto}'


# clase que contiene el diseño de la tabla OPR_SOLICITUD
class Opr_Solicitud(models.Model):
    usuario_solicitud = models.ForeignKey(User, on_delete=models.CASCADE)
    clave_solicitud = models.CharField(max_length=50)
    id_cliente_solicitud = models.ForeignKey(Cat_Cliente, on_delete=models.CASCADE, related_name="cliente_solicitud")
    id_equipo_solicitud = models.ForeignKey(Cat_Equipo, on_delete=models.CASCADE, related_name="equipo_solicitud")
    diagnostico_solicitud = models.CharField(max_length=500)
    fecha_creacion_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_modificacion_solicitud = models.DateTimeField(auto_now=True)
    fecha_baja_solicitud = models.DateField(null=True, blank=True)
    fecha_estimada_entrega_solicitud = models.DateField(null=True, blank=True)
    fecha_entrega_solicitud = models.DateField(null=True, blank=True)
    activo_solicitud = models.BooleanField(default=True)

    # Metodo STR regresa una cadena que muestra las columnas id|id_cliente|id_equipo
    def __str__(self):
        return f'Solicitud {self.id} {self.id_cliente_solicitud} {self.id_equipo_solicitud}'


# clase que contiene el diseño de la tabla OPR_COTIZACION
class Opr_Cotizacion(models.Model):
    clave_cotizacion = models.CharField(max_length=50)
    fecha_creacion_cotizacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion_cotizacion = models.DateTimeField(auto_now=True)
    id_cliente_cotizacion = models.ForeignKey(Cat_Cliente, on_delete=models.CASCADE, related_name="cliente_cotizacion")
    id_equipo_cotizacion = models.ForeignKey(Cat_Equipo, on_delete=models.CASCADE, related_name="equipo_cotizacion")
    productos_cotizacion = models.ManyToManyField(Cat_Producto, blank=True, related_name='productos')
    servicios_cotizacion = models.ManyToManyField(Cat_Servicio, blank=True, related_name='servicios')
    total_cotizacion = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    activo_cotizacion = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.total_cotizacion += Cat_Servicio.objects.all().aggregate(
            total_cotizacion=Sum('costo_servicio'))['total_cotizacion']

        # self.total_cotizacion += Opr_Cotizacion.objects.all().aggregate(
        #     total_cotizacion=Sum('productos_cotizacion__costo_producto'))['total_cotizacion']


        super(Opr_Cotizacion, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     queryset = Opr_Cotizacion.objects.filter(pk=self.pk).aggregate(
    #         total_cotizacion=Sum('productos_cotizacion__costo_producto'))
    #     self.total_cotizacion += queryset
        # productos = Cat_Producto.objects.all()
        # self.total_cotizacion += sum(productos.values_list('costo_producto', flat=True))
        #super(Opr_Cotizacion, self).save(*args, **kwargs)

    def __str__(self):
        return f'Cotizacion {self.clave_cotizacion}: {str(self.total_cotizacion)}'
