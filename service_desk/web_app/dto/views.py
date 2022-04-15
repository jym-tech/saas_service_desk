from rest_framework.response import Response
from web_app.models import Cat_Equipo, Cat_Cliente, Cat_Servicio, Cat_Producto, Opr_Solicitud
from web_app.dto.serializers import (Cat_Equipo_Serializado, Cat_Cliente_Serializado,
                                     Cat_Servicio_Serializado, Cat_Producto_Serializado,
                                     Opr_Solicitud_Serializado)
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

# Clases para crear los querys de consulta de la base de datos
# Class para mostrar la lista de elementos tipo PRODUCTO y crear un elemento tipo PRODUCTO - GENERICO
class producto_lista_Generico(generics.ListCreateAPIView):
    queryset = Cat_Producto.objects.all()
    serializer_class = Cat_Producto_Serializado

# Class para mostrar|actualizar|eliminar un elemento tipo PRODUCTO - GENERICO
class producto_detalle_Generico(generics.RetrieveDestroyAPIView):
    queryset = Cat_Producto.objects.all()
    serializer_class = Cat_Producto_Serializado
    lookup_field = 'id'

# Class para mostrar la lista de elementos tipo SERVICIO y crear un elemento tipo SERVICIO - GENERICO
class servicio_lista_Generico(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Cat_Servicio.objects.all()
    serializer_class = Cat_Servicio_Serializado

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return  self.create(request, *args, **kwargs)

# Class para mostrar la lista de elementos tipo SERVICIO y crear un elemento tipo SERVICIO - GENERICO
class servicio_detalle_Generico(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Cat_Servicio.objects.all()
    serializer_class = Cat_Servicio_Serializado
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


# Class para mostrar la lista de elementos tipo SOLICITUD y crear un elemento tipo SOLICITUD
class solicitud_listaAV(APIView):
    def get(self, request):
        solicitudes = Opr_Solicitud.objects.all()
        solicitudes_serializados = Opr_Solicitud_Serializado(solicitudes, many=True)
        return Response(solicitudes_serializados.data)

    def post(self, request):
        solicitudes_deserializados = Opr_Solicitud_Serializado(solicitudes, many=True)
        if solicitudes_deserializados.is_valid():
            solicitudes_deserializados.save()
            return Response(solicitudes_deserializados.data)
        else:
            return Response(solicitudes_deserializados.errors, status=status.HTTP_400_BAD_REQUEST)

# Class Views para mostrar|actualizar|eliminar un elemento tipo CLIENTE
class solicitud_detalleAV(APIView):
    def get(self, request, id):
        try:
            solicitud = Opr_Solicitud.objects.get(pk=id)
        except Opr_Solicitud.DoesNotExist:
            return Response({'error': 'Solicitud no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        solicitud_serializado = Opr_Solicitud_Serializado(solicitud)
        return Response(solicitud_serializado.data)

    def put(self, request, id):
        try:
            solicitud = Opr_Solicitud.objects.get(pk=id)
        except Opr_Solicitud.DoesNotExist:
            return Response({'error': 'Solicitud no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        solicitud_serializado = Opr_Solicitud_Serializado(solicitud, data=request.data)
        if solicitud_serializado.is_valid():
            solicitud_serializado.save()
            return Response(solicitud_serializado.data)
        else:
            return Response(solicitud_serializado.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            solicitud = Opr_Solicitud.objects.get(pk=id)
        except Opr_Solicitud.DoesNotExist:
            return Response({'error': 'Solicitud no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Class para mostrar la lista de elementos tipo PRODUCTO y crear un elemento tipo PRODUCTO
class producto_listaAV(APIView):
    def get(self, request):
        productos = Cat_Producto.objects.all()
        productos_serializados = Cat_Producto_Serializado(productos, many=True)
        return Response(productos_serializados.data)

    def post(self, request):
        productos_deserializados = Cat_Producto_Serializado(productos, many=True)
        if productos_deserializados.is_valid():
            productos_deserializados.save()
            return Response(productos_deserializados.data)
        else:
            return Response(productos_deserializados.errors, status=status.HTTP_400_BAD_REQUEST)

# Class para mostrar la lista de elementos tipo SERVICIO y crear un elemento tipo SERVICIO
class servicio_listaAV(APIView):
    def get(self, request):
        servicios = Cat_Servicio.objects.all()
        servicios_serializados = Cat_Servicio_Serializado(servicios, many=True)
        return Response(servicios_serializados.data)

    def post(self, request):
        servicios_deserializados = Cat_Servicio_Serializado(servicios, many=True)
        if servicios_deserializados.is_valid():
            servicios_deserializados.save()
            return Response(servicios_deserializados.data)
        else:
            return Response(servicios_deserializados.errors, status=status.HTTP_400_BAD_REQUEST)


# Class para mostrar la lista de elementos tipo CLIENTE y crear un elemento tipo CLIENTE
class cliente_listaAV(APIView):
    def get(self, request):
        clientes = Cat_Cliente.objects.all()
        clientes_serializados = Cat_Cliente_Serializado(clientes, many=True, context={'request': request})
        return Response(clientes_serializados.data)

    def post(self, request):
        clientes_deserializados = Cat_Cliente_Serializado(data=request.data, context={'request': request})
        if clientes_deserializados.is_valid():
            clientes_deserializados.save()
            return Response(clientes_deserializados.data)
        else:
            return Response(clientes_deserializados.errors, status=status.HTTP_400_BAD_REQUEST)

# Class Views para mostrar|actualizar|eliminar un elemento tipo CLIENTE
class cliente_detalleAV(APIView):
    def get(self, request, id):
        try:
            cliente = Cat_Cliente.objects.get(pk=id)
        except Cat_Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        cliente_serializado = Cat_Cliente_Serializado(cliente, context={'request': request})
        return Response(cliente_serializado.data)

    def put(self, request, id):
        try:
            cliente = Cat_Cliente.objects.get(pk=id)
        except Cat_Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        cliente_serializado = Cat_Cliente_Serializado(cliente, data=request.data)
        if cliente_serializado.is_valid():
            cliente_serializado.save()
            return Response(cliente_serializado.data)
        else:
            return Response(cliente_serializado.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            cliente = Cat_Cliente.objects.get(pk=id)
        except Cat_Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Class para mostrar la lista de elementos tipo EQUIPO y crear un elemento tipo EQUIPO
class equipo_listaAV(APIView):
    def get(self, request):
        equipos = Cat_Equipo.objects.all() # Guarda el listado de los todos los elementos de tipo EQUIPO
        equipos_serializados = Cat_Equipo_Serializado(equipos, many=True, context={'request': request}) # Serializa toda la informacion tipo EQUIPO
        return Response(equipos_serializados.data) # Devuelve los datos serializados en un formato tipo JSON

    def post(self, request):
        equipos_deserializados = Cat_Equipo_Serializado(data=request.data, context={'request': request})
        if equipos_deserializados.is_valid():
            equipos_deserializados.save()
            return Response(equipos_deserializados.data)
        else:
            return Response(equipos_deserializados.errors, status=status.HTTP_400_BAD_REQUEST)

# Class Views para mostrar|actualizar|eliminar un elemento tipo EQUIPO
class equipo_detalleAV(APIView):
    def get(self, request, id):
        try:
            equipo = Cat_Equipo.objects.get(pk=id)
        except Cat_Equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        equipo_serializado = Cat_Equipo_Serializado(equipo, context={'request': request})
        return Response(equipo_serializado.data)

    def put(self, request, id):
        try:
            equipo = Cat_Equipo.objects.get(pk=id)
        except Cat_Equipo.DoesNotExist:
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
        except Cat_Equipo.DoesNotExist:
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
