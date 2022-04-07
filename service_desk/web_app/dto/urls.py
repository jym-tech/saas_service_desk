from django.urls import path
#from web_app.dto.views import equipo_lista, equipo_detalle
from web_app.dto.views import equipo_listAV, equipo_detalleAV

urlpatterns = [
    path('lista/', equipo_listAV.as_view()),
    path('<int:id>', equipo_detalleAV.as_view()),
]