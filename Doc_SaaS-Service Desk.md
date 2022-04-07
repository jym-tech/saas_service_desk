# Proyecto: SaaS-Service Desk

#### service_desk

###### settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web_app',
    'rest_framework',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'saas_db',
        'USER': 'root',
        'PASSWORD': 'S0p0rt3',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

###### urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipo/', include('web_app.urls')),
]
```

#### web_app

###### models.py

```python
from django.db import models

class Cat_Equipo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100)
    num_parte = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    disco = models.CharField(max_length=100)
    comentario = models.CharField(max_length=255)

    def __str__(self):
        return f'Equipo {self.id}: {self.marca} {self.modelo}'
```

###### admin.py

```python
from django.contrib import admin
from web_app.models import Cat_Equipo

admin.site.register(Cat_Equipo)
```

###### dto/urls.py

```python
from django.urls import path
from web_app.dto.views import equipo_listAV, equipo_detalleAV

urlpatterns = [
    path('lista/', equipo_listAV.as_view()),
    path('<int:id>', equipo_detalleAV.as_view()),
]
```

###### dto/views.py

```python
from rest_framework.response import Response
from web_app.models import Cat_Equipo
from web_app.dto.serializers import Cat_Equipo_Serializado
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
```

###### dto/serializers.py

```python

```

### Comandos

```shell
venv\Scripts\activate
python -m pip install django
python -m pip install --upgrade pip
django-admin version
pip install mysql-connector-python
pip install mysqlclient
pip install djangorestframework
pip freeze
django-admin startproject service_desk
python manage.py startapp web_app
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
