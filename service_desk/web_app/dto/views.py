from rest_framework.response import Response
from web_app.models import Cat_Equipo
from web_app.dto.serializers import Cat_Equipo_Serializado
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class equipo_listAV(APIView):
    def get(self, request):
        equipos = Cat_Equipo.objects.all()
        equipos_serializados = Cat_Equipo_Serializado(equipos, many=True)
        return Response(equipos_serializados.data)

    def post(self, request):
        equipos_deserializados = Cat_Equipo_Serializado(data=request.data)
        if equipos_deserializados.is_valid():
            equipos_deserializados.save()
            return Response(equipos_deserializados.data)
        else:
            return Response(equipos_deserializados.errors, status=status.HTTP_400_BAD_REQUEST)

class equipo_detalleAV(APIView):
    def get(self, request, id):
        try:
            equipo = Cat_Equipo.objects.get(pk=id)
        except equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        equipo_serializado = Cat_Equipo_Serializado(equipo)
        return Response(equipo_serializado.data)

    def put(self, request, id):
        try:
            equipo = Cat_Equipo.objects.get(pk=id)
        except equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        equipo_serializado = Cat_Equipo_Serializado(equipo, data=request.data)
        if equipo_serializado.is_valid():
            equipo_serializado.save()
            return Response(equipo_serializado.data)
        else:
            return Response(equipo_serializado.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            equipo = Cat_Equipo.objects.get(pk=id)
        except equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def equipo_lista(request):
#     if request.method == 'GET':
#         equipos = Cat_Equipo.objects.all()
#         equipos_serializado = Cat_Equipo_Serializado(equipos, many=True)
#         return Response(equipos_serializado.data)
#
#     if request.method == 'POST':
#         equipos_deserializado = Cat_Equipo_Serializado(data=request.data)
#         if equipos_deserializado.is_valid():
#             equipos_deserializado.save()
#             return Response(equipos_deserializado.data)
#         else:
#             return Response(equipos_deserializado.errors)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def equipo_detalle(request, id):
#     if request.method == 'GET':
#         try:
#             equipo = Cat_Equipo.objects.get(pk=id)
#             equipo_serializado = Cat_Equipo_Serializado(equipo)
#             return Response(equipo_serializado.data)
#         except Cat_Equipo.DoesNotExist:
#             return Response({'Error': 'El equipo no existe'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         equipo = Cat_Equipo.objects.get(pk=id)
#         equipo_deserializado = Cat_Equipo_Serializado(equipo, data=request.data)
#         if equipo_deserializado.is_valid():
#             equipo_deserializado.save()
#             return  Response(equipo_deserializado.data)
#         else:
#             return  Response(equipo_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         try:
#             equipo = Cat_Equipo.objects.get(pk=id)
#             equipo.delete()
#         except Cat_Equipo.DoesNotExist:
#             return Response({'Error': 'El equipo no existe'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_204_NO_CONTENT)
