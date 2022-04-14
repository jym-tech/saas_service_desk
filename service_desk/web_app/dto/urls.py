from django.urls import path
#from web_app.dto.views import equipo_lista, equipo_detalle
from web_app.dto.views import equipo_listaAV, equipo_detalleAV, cliente_listaAV, cliente_detalleAV, servicio_listaAV, producto_listaAV, solicitud_listaAV, solicitud_detalleAV

# Registro de la coleccion de URL para mostrar la lista|agregar elementos
# asi como agregar|modificar|eliminar un elemento especifico
urlpatterns = [
    path('equipo/', equipo_listaAV.as_view(), name='equipo'),
    path('equipo/<int:id>', equipo_detalleAV.as_view(), name='equipo_detail'),
    path('cliente/', cliente_listaAV.as_view(), name='cliente'),
    path('cliente/<int:id>', cliente_detalleAV.as_view(), name='cliente_detail'),
    path('servicio/', servicio_listaAV.as_view(), name='servicio'),
    path('producto/', producto_listaAV.as_view(), name='servicio_detail'),
    path('solicitud/', solicitud_listaAV.as_view(), name='solicitud'),
    path('solicitud/<int:id>', solicitud_detalleAV.as_view(), name='solicitud_detail')
]