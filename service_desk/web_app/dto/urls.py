from django.urls import path
# from web_app.dto.views import equipo_lista, equipo_detalle
from web_app.dto.views import (equipo_listaAV, equipo_detalleAV, cliente_listaAV, cliente_detalleAV,
                               servicio_listaAV, producto_listaAV, solicitud_listaAV, solicitud_detalleAV,
                               servicio_lista_Generico, servicio_detalle_Generico, producto_lista_Generico,
                               producto_detalle_Generico)

# Registro de la coleccion de URL para mostrar la lista|agregar elementos
# asi como agregar|modificar|eliminar un elemento especifico
urlpatterns = [
    path('equipo/', equipo_listaAV.as_view(), name='equipo-list'),
    path('equipo/<int:id>', equipo_detalleAV.as_view(), name='equipo-detail'),
    path('cliente/', cliente_listaAV.as_view(), name='cliente-list'),
    path('cliente/<int:id>', cliente_detalleAV.as_view(), name='cliente-detail'),
    path('servicio/', servicio_lista_Generico.as_view(), name='servicio-list'),
    path('servicio/<int:id>', servicio_detalle_Generico.as_view(), name='servicio-detail'),
    path('producto/', producto_lista_Generico.as_view(), name='producto-list'),
    path('producto/<int:id>', producto_detalle_Generico.as_view(), name='producto-detail'),
    path('solicitud/', solicitud_listaAV.as_view(), name='solicitud-list'),
    path('solicitud/<int:id>', solicitud_detalleAV.as_view(), name='solicitud-detail')
]