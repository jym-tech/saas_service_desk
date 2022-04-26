from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.dto.views import registro_view


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('registro/', registro_view, name='registro')
]