from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.dto.serializers import RegistroSerializado
from rest_framework.authtoken.models import Token
from user_app import models


@api_view(['POST',])
def registro_view(request):
    if request.method == 'POST':
        registro = RegistroSerializado(data=request.data)
        datos = {}
        if registro.is_valid():
            cuenta = registro.save()
            datos['response'] = 'El registro del usuario fue exitoso'
            datos['username'] = cuenta.username
            datos['email'] = cuenta.email
            token = Token.objects.get(user=cuenta).key
            datos['token'] = token

            # return Response(registro.data)
        else:
            datos = registro.errors

        return Response(datos)