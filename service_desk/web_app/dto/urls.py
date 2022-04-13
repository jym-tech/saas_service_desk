from django.urls import path
#from web_app.dto.views import equipo_lista, equipo_detalle
from web_app.dto.views import equipo_listaAV, equipo_detalleAV, cliente_listaAV, servicio_listaAV, producto_listaAV, solicitud_listaAV

# Registro de la coleccion de URL para mostrar la lista|agregar elementos
# asi como agregar|modificar|eliminar un elemento especifico
urlpatterns = [
    path('equipos/', equipo_listaAV.as_view()),
    path('equipos/<int:id>', equipo_detalleAV.as_view()),
    path('clientes/', cliente_listaAV.as_view()),
    path('servicios/', servicio_listaAV.as_view()),
    path('productos/', producto_listaAV.as_view()),
    path('solicitudes/', solicitud_listaAV.as_view()),
]