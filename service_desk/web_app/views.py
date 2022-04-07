# from django.shortcuts import render
# from django.http import JsonResponse
# from web_app.models import Cat_Equipo
#
# # Create your views here.
# def equipo_lista(request):
#     equipos = Cat_Equipo.objects.all()
#     datos_equipos = {
#         'equipos': list(equipos.values())
#     }
#     return JsonResponse(datos_equipos)
#
# def equipo_detalle(request, id):
#     equipo = Cat_Equipo.objects.get(pk=id)
#     datos_equipo = {
#         'modelo': equipo.modelo,
#         'marca': equipo.marca,
#         'num_serie': equipo.num_serie,
#         'num_parte': equipo.num_parte,
#         'procesador': equipo.procesador,
#         'ram': equipo.ram,
#         'disco': equipo.disco,
#         'comentario': equipo.comentario,
#     }
#     return JsonResponse(datos_equipo)