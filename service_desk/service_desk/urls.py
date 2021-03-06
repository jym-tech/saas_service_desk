"""service_desk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Creacion de URL principal para acceder a los metodos en el archivo views.py
urlpatterns = [
    # Path de administracion de Django Rest Framework
    path('admin/', admin.site.urls),

    # Path de la aplicacion principal
    path('app/', include('web_app.dto.urls')),

    # Login de RestFramework
    # path('api-auth', include('rest_framework.urls')),

    # Path para login de usuario
    path('cuenta/', include('user_app.dto.urls')),
]
