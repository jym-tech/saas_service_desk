from django.contrib import admin

# Register your models here.
from web_app.models import Cat_Equipo, Cat_Cliente, Cat_Servicio, Cat_Producto, Opr_Solicitud, Opr_Cotizacion

# Registro del modelo CAT_EQUIPO
admin.site.register(Cat_Equipo)

# Registro del modelo CAT_CLIENTE
admin.site.register(Cat_Cliente)

# Registro del modelo CAT_SERVICIO
admin.site.register(Cat_Servicio)

# Registro del modelo CAT_PRODUCTO
admin.site.register(Cat_Producto)

# Registro del modelo OPR_SOLICITUD
admin.site.register(Opr_Solicitud)

# Registro del modelo OPR_COTIZACION
admin.site.register(Opr_Cotizacion)
