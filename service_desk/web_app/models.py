from django.db import models


# Create your models here.
# Crear el modelo de la tabla que corresponda con cada entidad de la Base de Datos
# clase que contiene el diseño de la tabla CAT_EQUIPO
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
    activo_servicio = models.BooleanField(default=True)

    # Metodo STR regresa una cadena que muestra las columnas id|descripcion
    def __str__(self):
        return f'Servicio {self.id} {self.tipo_servicio}'

# clase que contiene el diseño de la tabla CAT_PRODUCTO
class Cat_Producto(models.Model):
    sku_producto = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50)
    descripcion_producto = models.CharField(max_length=500)
    activo_producto = models.BooleanField(default=True)

    # Metodo STR regresa una cadena que muestra las columnas id|descripcion
    def __str__(self):
        return f'Producto {self.id} {self.descripcion_producto}'

# clase que contiene el diseño de la tabla OPR_SOLICITUD
class Opr_Solicitud(models.Model):
    clave_solicitud = models.CharField(max_length=50)
    id_cliente_solicitud = models.ForeignKey(Cat_Cliente, on_delete=models.PROTECT, related_name="idCliente")
    id_equipo_solicitud = models.ForeignKey(Cat_Equipo, on_delete=models.PROTECT, related_name="idEquipo")
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